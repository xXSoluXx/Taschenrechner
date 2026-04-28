import tkinter as tk
from tkinter import font

last_size = None

def start_app(controller):
    """
    Startet die Tkinter-Taschenrechner-App.

    Args:
        controller: Ein Objekt, das Rechenlogik bereitstellt
                    (z.B. calculate, square, reciprocal, square_root).
    """
    error_state = False


    root = tk.Tk()
    root.title("Taschenrechner")

    root.geometry("320x365")   # Startgröße
    root.minsize(320, 365)     # Minimum

    # ---------------- DISPLAY ----------------
    display_frame = tk.Frame(root, height=75)
    display_frame.grid(row=0, column=0, columnspan=4, sticky="ew")
    display_frame.grid_propagate(False)  # verhindert Größenänderung
    display_frame.pack_propagate(False)    # zusätzlich stabilisieren

    display_font = font.Font(family="Arial", size=28, weight="bold")

    display = tk.Entry(display_frame, justify="right", font=display_font, border=0, relief="flat")
    display.pack(fill="both", expand=True)

    display.insert(0, "0")  # Startwert beim öffnen

    def set_font(size):
        global last_size
        if size != last_size:
            display_font.configure(size=size)
            last_size = size


    def update_display(value):
        """Aktualisiert die Anzeige mit einem neuen Wert."""
        nonlocal error_state

        value = str(value)

        if value.lower() in [
    "error",
    "ungültige eingabe",
    "nicht durch 0 teilbar",
    "error(negative zahl)",
    "unbekannter fehler",
    "ungültiger ausdruck"
]:
            
            error_state = True
        else:
            error_state = False

        max_length = 21
        if len(value) > max_length:
            value = value[:max_length]

        display.delete(0, "end")
        display.insert(0, value)

        length = len(value)

        base_size = 28
        min_size = 14
        threshold = 10

        if length <= threshold:
            size = base_size
        else:
            size = base_size - (length - threshold)
            if size < min_size:
                size = min_size

        set_font(size)
        display.icursor(tk.END)

    def calculate():
        """Berechnet den aktuellen Ausdruck über den Controller."""
        result = controller.calculate(display.get())
        update_display(result)

    # ---------------- EINGABE ----------------
    def click(value):
        """Fügt ein Zeichen in das Display ein."""
        nonlocal error_state

        if error_state:
            display.delete(0, "end")
            display.insert(0, "0")
            error_state = False

        current = display.get()

        if current == "0":
            display.delete(0, "end")

        display.insert(tk.END, value)
        update_display(display.get())

    def backspace():
        """Löscht das letzte Zeichen (⌫)."""
        nonlocal error_state

        if error_state:
            display.delete(0, "end")
            display.insert(0, "0")
            error_state = False
            set_font(28)
            return

        current_text = display.get()

        if len(current_text) <= 1:
            display.delete(0, "end")
            display.insert(0, "0")
        else:
            display.delete(0, "end")
            display.insert(0, current_text[:-1])

        update_display(display.get())

    def clear():
        """Löscht den gesamten Inhalt (C)."""
        nonlocal error_state
        display.delete(0, "end")
        display.insert(0, "0")
        error_state = False
        set_font(28)

    def clear_entry():
        """Löscht nur die aktuelle Eingabe (CE)."""
        nonlocal error_state

        if error_state:
            display.delete(0, "end")
            display.insert(0, "0")
            error_state = False
            set_font(28)
            return

        current = display.get()

        for op in ["+", "-", "*", "/"]:
            if op in current:
                a, _ = current.split(op)
                display.delete(0, "end")
                display.insert(0, a + op)
                update_display(display.get())
                return

        # Wenn kein Operator vorhanden → auf 0 setzen
        display.delete(0, "end")
        display.insert(0, "0")
        set_font(28)

    # ---------------- MATHE-FUNKTIONEN ----------------
    def square():
        """Berechnet das Quadrat einer Zahl (x²)."""
        value = display.get()
        result = controller.square(value)
        update_display(result)

    def reciprocal():
        """Berechnet den Kehrwert (1/x)."""
        value = display.get()
        result = controller.reciprocal(value)
        update_display(result)

    def square_root():
        """Berechnet die Quadratwurzel (√x)."""
        value = display.get()
        result = controller.square_root(value)
        update_display(result)

    def toggle_sign():
        """Wechselt das Vorzeichen (+/-)."""
        value = display.get()

        if not value:
            return

        if value.startswith("-"):
            value = value[1:]
        else:
            value = "-" + value

        update_display(value)

    # ---------------- BUTTONS ----------------

    tk.Button(root, text="%", width=7, height=2, font=("Arial", 12),
              command=lambda: click("%")).grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="CE", width=7, height=2, font=("Arial", 12),
              command=clear_entry).grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="C", width=7, height=2, font=("Arial", 12),
              command=clear).grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="⌫", width=7, height=2, font=("Arial", 12),
              command=backspace).grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="1/x", width=7, height=2, font=("Arial", 12),
              command=reciprocal).grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="x²", width=7, height=2, font=("Arial", 12),
              command=square).grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="²√x", width=7, height=2, font=("Arial", 12),
              command=square_root).grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="÷", width=7, height=2, font=("Arial", 12),
              command=lambda: click("/")).grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

    # ---------------- ZAHLEN ----------------
    tk.Button(root, text="7", width=7, height=2, font=("Arial", 12),
              command=lambda: click("7")).grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="8", width=7, height=2, font=("Arial", 12),
              command=lambda: click("8")).grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="9", width=7, height=2, font=("Arial", 12),
              command=lambda: click("9")).grid(row=3, column=2, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="x", width=7, height=2, font=("Arial", 12),
              command=lambda: click("*")).grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="4", width=7, height=2, font=("Arial", 12),
              command=lambda: click("4")).grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="5", width=7, height=2, font=("Arial", 12),
              command=lambda: click("5")).grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="6", width=7, height=2, font=("Arial", 12),
              command=lambda: click("6")).grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="-", width=7, height=2, font=("Arial", 12),
              command=lambda: click("-")).grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="1", width=7, height=2, font=("Arial", 12),
              command=lambda: click("1")).grid(row=5, column=0, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="2", width=7, height=2, font=("Arial", 12),
              command=lambda: click("2")).grid(row=5, column=1, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="3", width=7, height=2, font=("Arial", 12),
              command=lambda: click("3")).grid(row=5, column=2, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="+", width=7, height=2, font=("Arial", 12),
              command=lambda: click("+")).grid(row=5, column=3, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="+/-", width=7, height=2, font=("Arial", 12),
              command=toggle_sign).grid(row=6, column=0, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="0", width=7, height=2, font=("Arial", 12),
              command=lambda: click("0")).grid(row=6, column=1, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text=",", width=7, height=2, font=("Arial", 12),
              command=lambda: click(",")).grid(row=6, column=2, sticky="nsew", padx=2, pady=2)

    tk.Button(root, text="=", width=7, height=2, font=("Arial", 12),
              command=calculate).grid(row=6, column=3, sticky="nsew", padx=2, pady=2)

    for i in range(7):
        if i == 0:
            root.rowconfigure(i, weight=0)  # Display bleibt fix
        else:
            root.rowconfigure(i, weight=1)  # Buttons wachsen


    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)

    # ---------------- START ----------------
    root.mainloop()