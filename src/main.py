from model.calculator import Calculator
from controller.controller import Controller
from view.tkinter_view import start_app

def main():
    calc = Calculator()
    controller = Controller(calc)

    start_app(controller)

if __name__ == "__main__":
    main()