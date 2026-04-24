from model.validate_input import validate_input


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_inputs(self):
        try:
            a = self.view.get_input()
            a = validate_input(a)
            op = self.view.get_operation()
            # Wurzel separat behandeln
            if op == "w":
                result = self.model.root(a)
                self.view.display_root(a, result)
                return
            b = self.view.get_input()
            b = validate_input(b)
            
            return a, op, b
        except (TypeError, ValueError) as e:
            self.view.display_error(str(e))
            return None, None, None

    def process_operation(self, a, b, op):
        # Division extra prüfen
        if op in ["/", "%"] and b == 0:
            self.view.display_error("Division durch 0 nicht erlaubt")
            return

        # normale Operationen
        operations = {
            "+": self.model.add,
            "-": self.model.subtract,
            "*": self.model.multiply,
            "/": self.model.divide,
            "%": self.model.modulo,
            "**": self.model.potenz,
            "^": self.model.potenz
        }

        if op not in operations:
            self.view.display_error("Ungültige Operation")
            return

        result = operations[op](a, b)
        self.view.display_result(a, b, op, result)

    def run(self):
        while True:
            a, op, b = self.handle_inputs()
            
            if a is not None:
                self.process_operation(a, b, op)

            if not self.view.ask_continue():
                break 