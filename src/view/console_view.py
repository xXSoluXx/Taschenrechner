import model.format_result

class View:

    def get_input(self):
        return input("\nZahl eingeben: ")
    
    def get_operation(self):
        return input("\nRechenoperation auswählen:\n\n(Addition(+)\nSubtraktion(-)\nMultiplikation(*)\nDivision(/)\nModulo(%)\nPotenz(^)\nWurzel(w)")

    def display_result(self, a, b, op, result):
        result = model.format_result.format_result(result)
        print(f"\nErgebnis:\n{a} {op} {b} = {result}")


    def display_root(self, a, result):
        result = model.format_result.format_result(result)
        print(f"\nErgebnis:\n√{a} = {result}")

    def display_error(self, message):
        print(f"\nFehler: {message}") 

    

    def ask_continue(self):
        while True:
            print("\nMöchten Sie eine weitere Berechnung durchführen?")
            print("[Ja]  -> Neue Berechnung")
            print("[Nein] -> Programm beenden")
            
            choice = input("\nDeine Wahl > ").lower()
            
            if choice == "ja":
                return True
            elif choice == "nein":
                return False
            else:
                print("Ungültige Eingabe. Bitte JA oder Nein eingeben.")
