import tkinter as tk

root = tk.Tk()
root.title("Taschenrechner")

# Anzeige (Display)
display = tk.Entry(root, width=15, font=("Arial", 28))
display.grid(row=0, column=0, columnspan=16)

# Funktion für Buttons
def click(value):
    display.insert(tk.END, value)

# Buttons

tk.Button(root, text="%", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("%")).grid(row=1, column=0)

tk.Button(root, text="CE", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("CE")).grid(row=1, column=1)

tk.Button(root, text="C", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("C")).grid(row=1, column=2)

tk.Button(root, text="⌫", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("⌫")).grid(row=1, column=3)


tk.Button(root, text="1/x", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("1/x")).grid(row=2, column=0)

tk.Button(root, text="x²", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("x²")).grid(row=2, column=1)

tk.Button(root, text="²√x", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("²√x")).grid(row=2, column=2)

tk.Button(root, text="÷", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("/")).grid(row=2, column=3)


tk.Button(root, text="7", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("7")).grid(row=3, column=0)

tk.Button(root, text="8", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("8")).grid(row=3, column=1)

tk.Button(root, text="9", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("9")).grid(row=3, column=2)

tk.Button(root, text="x", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("*")).grid(row=3, column=3)


tk.Button(root, text="4", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("4")).grid(row=4, column=0)

tk.Button(root, text="5", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("5")).grid(row=4, column=1)

tk.Button(root, text="6", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("6")).grid(row=4, column=2)

tk.Button(root, text="-", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("-")).grid(row=4, column=3)


tk.Button(root, text="1", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("1")).grid(row=5, column=0)

tk.Button(root, text="2", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("2")).grid(row=5, column=1)

tk.Button(root, text="3", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("3")).grid(row=5, column=2)

tk.Button(root, text="+", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("+")).grid(row=5, column=3)


tk.Button(root, text="+/-", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("-")).grid(row=6, column=0)

tk.Button(root, text="0", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("0")).grid(row=6, column=1)

tk.Button(root, text=",", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click(".")).grid(row=6, column=2)

tk.Button(root, text="=", width=7, height=2, font=("Arial", 12), padx=4,
          command=lambda: click("=")).grid(row=6, column=3)



root.mainloop()