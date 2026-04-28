from model.calculator import Calculator
from controller.controller import Controller
from view.tkinter_view import start_app

def main():
    calc = Calculator()
    controller = Controller(calc)

    start_app(controller)

if __name__ == "__main__":
    main()


    # Prozentberechnung macht noch fehler muss behoben werden (Erledigt)
    # Responsible machen (Erledigt)
    # beim starten soll immer schon die 0 angezeigt werden (Erledigt)
    # bei fehlermeldung soll durch klicken von cd, c und back soll die fehlermeldung entfernt werden,
    # bzw dann mit dem klicken auf eine neue zahl direkt normal weitergerechnet werden (Erledigt)

    
    # Nach jedem 4 Zeichen soll ein Punkt gesetzt werden um zu signalisieren das es tausend sind
    # Layout schöner Gestalten 