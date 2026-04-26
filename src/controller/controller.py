from model.validate_input import validate_input


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # hier wird der controller neum implementiert und mit der neuen GUI-Klasse und dem model verbunden