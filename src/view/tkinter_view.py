import tkinter as tk


def start_app(controller):
    """
    Startet die Tkinter-Taschenrechner-App.

    Args:
        controller: Ein Objekt, das Rechenlogik bereitstellt
                    (z.B. calculate, square, reciprocal, square_root).
    """

    root = tk.Tk()
    root.title("Taschenrechner")

    # ---------------- DISPLAY ----------------
    display = tk.Entry(root, width=15, justify="right", font=("Arial", 28))
    display.grid(row=0, column=0, columnspan=16)

    def update_display(value):
        """Aktualisiert die Anzeige mit einem neuen Wert."""
        display.delete(0, "end")
        display.insert(0, value)

    def calculate():
        """Berechnet den aktuellen Ausdruck über den Controller."""
        result = controller.calculate(display.get())
        update_display(result)

    # ---------------- EINGABE ----------------
    def click(value):
        """Fügt ein Zeichen in das Display ein."""
        display.insert(tk.END, value)

    def backspace():
        """Löscht das letzte Zeichen (⌫)."""
        current_text = display.get()
        display.delete(0, "end")
        display.insert(0, current_text[:-1])

    def clear():
        """Löscht den gesamten Inhalt (C)."""
        display.delete(0, "end")

    def clear_entry():
        """Löscht nur die aktuelle Eingabe (CE)."""
        display.delete(0, "end")

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
              command=lambda: click("%")).grid(row=1, column=0)

    tk.Button(root, text="CE", width=7, height=2, font=("Arial", 12),
              command=clear_entry).grid(row=1, column=1)

    tk.Button(root, text="C", width=7, height=2, font=("Arial", 12),
              command=clear).grid(row=1, column=2)

    tk.Button(root, text="⌫", width=7, height=2, font=("Arial", 12),
              command=backspace).grid(row=1, column=3)

    tk.Button(root, text="1/x", width=7, height=2, font=("Arial", 12),
              command=reciprocal).grid(row=2, column=0)

    tk.Button(root, text="x²", width=7, height=2, font=("Arial", 12),
              command=square).grid(row=2, column=1)

    tk.Button(root, text="²√x", width=7, height=2, font=("Arial", 12),
              command=square_root).grid(row=2, column=2)

    tk.Button(root, text="÷", width=7, height=2, font=("Arial", 12),
              command=lambda: click("/")).grid(row=2, column=3)

    # ---------------- ZAHLEN ----------------
    tk.Button(root, text="7", width=7, height=2, font=("Arial", 12),
              command=lambda: click("7")).grid(row=3, column=0)

    tk.Button(root, text="8", width=7, height=2, font=("Arial", 12),
              command=lambda: click("8")).grid(row=3, column=1)

    tk.Button(root, text="9", width=7, height=2, font=("Arial", 12),
              command=lambda: click("9")).grid(row=3, column=2)

    tk.Button(root, text="x", width=7, height=2, font=("Arial", 12),
              command=lambda: click("*")).grid(row=3, column=3)

    tk.Button(root, text="4", width=7, height=2, font=("Arial", 12),
              command=lambda: click("4")).grid(row=4, column=0)

    tk.Button(root, text="5", width=7, height=2, font=("Arial", 12),
              command=lambda: click("5")).grid(row=4, column=1)

    tk.Button(root, text="6", width=7, height=2, font=("Arial", 12),
              command=lambda: click("6")).grid(row=4, column=2)

    tk.Button(root, text="-", width=7, height=2, font=("Arial", 12),
              command=lambda: click("-")).grid(row=4, column=3)

    tk.Button(root, text="1", width=7, height=2, font=("Arial", 12),
              command=lambda: click("1")).grid(row=5, column=0)

    tk.Button(root, text="2", width=7, height=2, font=("Arial", 12),
              command=lambda: click("2")).grid(row=5, column=1)

    tk.Button(root, text="3", width=7, height=2, font=("Arial", 12),
              command=lambda: click("3")).grid(row=5, column=2)

    tk.Button(root, text="+", width=7, height=2, font=("Arial", 12),
              command=lambda: click("+")).grid(row=5, column=3)

    tk.Button(root, text="+/-", width=7, height=2, font=("Arial", 12),
              command=toggle_sign).grid(row=6, column=0)

    tk.Button(root, text="0", width=7, height=2, font=("Arial", 12),
              command=lambda: click("0")).grid(row=6, column=1)

    tk.Button(root, text=",", width=7, height=2, font=("Arial", 12),
              command=lambda: click(",")).grid(row=6, column=2)

    tk.Button(root, text="=", width=7, height=2, font=("Arial", 12),
              command=calculate).grid(row=6, column=3)

    # ---------------- START ----------------
    root.mainloop()