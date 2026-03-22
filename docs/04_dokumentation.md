# Taschenrechner V.0.1.0

## Beschreibung
Ein modular aufgebauter Konsolen-Taschenrechner zur Durchführung grundlegender mathematischer Operationen.  
Das Projekt verwendet die **MVC-Architektur**, sodass spätere Erweiterungen wie GUI oder zusätzliche Funktionen problemlos möglich sind.

---

## Ziel
Der Taschenrechner soll:

- Zwei Zahlen einlesen
- Eine Rechenoperation (+, -, *, /) auswählen
- Das Ergebnis korrekt berechnen
- Fehler bei ungültigen Eingaben oder Division durch 0 erkennen und anzeigen

---

## Hauptfunktionen
- Addition, Subtraktion, Multiplikation, Division
- Konsoleneingabe von zwei Zahlen
- Auswahl der Rechenoperation
- Ausgabe des Ergebnisses
- Fehlerbehandlung:
  - Ungültige Eingaben
  - Division durch 0

---

## Architektur (MVC)

**Model:**  
- Verantwortlich für die Berechnungslogik (`Calculator`)

**View:**  
- Verantwortlich für die Ein- und Ausgabe (`console_view.py`)  

**Controller:**  
- Steuert die Programmlogik (`Controller`)  
- Trennt Input, Berechnung und Ausgabe
- Methoden:
  - `handle_inputs()`
  - `process_operation()`
  - `run()`

---

## Komponenten
|----------------------------------------------------------------------------------------|
|    Komponente   |                           Beschreibung                               |
|-----------------|----------------------------------------------------------------------|
| `Calculator`    | Berechnungen: add, subtract, multiply, divide                        |
| `View`          | Benutzerinteraktion: Eingabe, Ausgabe, Fehleranzeige                 |
| `Controller`    | Steuerung: Inputs abfragen, Operation durchführen, Ergebnis anzeigen |
|----------------------------------------------------------------------------------------|

---

## Datenfluss


Benutzer
│
▼
View (console_view.py)
│
▼
Controller (Controller)
│
▼
Model (Calculator)
│
▼
Controller
│
▼
View
│
▼
Benutzer


---

## Klassendesign

**Calculator (Model)**  
- `add(a, b)`  
- `subtract(a, b)`  
- `multiply(a, b)`  
- `divide(a, b)`  

**View (View)**  
- `get_input()`  
- `get_operation()`  
- `display_result(result)`  
- `display_error(message)`  

**Controller (Controller)**  
- `handle_inputs()`  
- `process_operation(a, b, op)`  
- `run()`  

---

## Technologien
- Sprache: Python  
- Framework: keine (Konsolenanwendung)  
- Tools: VS Code, Python Interpreter  

---

## Scope
- Nur Konsolenanwendung  
- Keine komplexen mathematischen Funktionen (Sinus, Logarithmus etc.)  
- Keine Speicherung von Ergebnissen  
- Keine Mehrfachberechnungen in einer Eingabe  

---

## Edge Cases
- Division durch 0  
- Ungültige Eingaben (Text statt Zahlen)  
- Leere Eingaben  
- Sehr große oder sehr kleine Zahlen  

---

## Zukünftige Erweiterungen
- GUI (z. B. Tkinter oder Qt)  
- Prozentrechnung und Potenzen  
- Verlauf (History) speichern  
- Mehrere Berechnungen hintereinander