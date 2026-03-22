class View:
    def get_input(self):
        return input("Zahl eingeben: ")
    
    def get_operation(self):
        return input("Rechenoperation auswählen (+ - * /): ")

    def display_result(self, result):
        print(f"Ergebnis: {result}")

    def display_error(self, message):
        print(f"Fehler: {message}") 

