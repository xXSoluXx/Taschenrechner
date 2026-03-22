class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_inputs(self):
        """Fragt den Nutzer nach zwei Zahlen und der Operation."""
        try:
            a = float(self.view.get_input())
            op = self.view.get_operation()
            b = float(self.view.get_input())
            
            return a, op, b
        except ValueError:
            self.view.display_error("Ungültige Eingabe. Bitte Zahlen eingeben.")
            return None, None, None

    def process_operation(self, a, b, op):
        """Führt die gewählte Operation aus und zeigt das Ergebnis an."""
        if op == "+":
            result = self.model.add(a, b)
        elif op == "-":
            result = self.model.subtract(a, b)
        elif op == "*":
            result = self.model.multiply(a, b)
        elif op == "/":
            if b == 0:
                self.view.display_error("Division durch 0 nicht erlaubt")
                return
            result = self.model.divide(a, b)
        else:
            self.view.display_error("Ungültige Operation")
            return
        self.view.display_result(result)

    def run(self):
        """Hauptfunktion, die alles steuert."""
        a, op, b = self.handle_inputs()
        if a is not None:
            self.process_operation(a, b, op) 