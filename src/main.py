from model.calculator import Calculator         # deine Datei calculator.py
from view.console_view import View              # deine Datei console_view.py
from controller.controller import Controller


def main():
    model = Calculator()
    view = View()
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main() 