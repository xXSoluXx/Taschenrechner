# Taschenrechner V.0.1.0

## Beschreibung
Ein modular aufgebauter Taschenrechner mit grafischer Benutzeroberfläche (GUI) zur Durchführung grundlegender und erweiterter mathematischer Operationen.  

Das Projekt verwendet die **MVC-Architektur (Model-View-Controller)**, sodass Erweiterungen wie neue Funktionen oder UI-Anpassungen einfach möglich sind.

---

## Ziel
Der Taschenrechner soll:

- Zahlen über Buttons eingeben können  
- Rechenoperationen auswählen (+, -, ×, ÷)  
- Erweiterte Funktionen ausführen (% , 1/x, xʸ, √, +/-)  
- Ergebnisse korrekt berechnen und anzeigen  
- Eingaben bearbeiten können (⌫, CE, C)  
- Fehler bei ungültigen Eingaben erkennen und anzeigen  

---

## Hauptfunktionen

### Eingabe
- Zahlen (0–9)  
- Dezimalzahlen (.)  
- Eingabe über GUI-Buttons  

---

### Rechenoperationen
- Addition  
- Subtraktion  
- Multiplikation  
- Division  

---

### Erweiterte Funktionen
- Prozent (%)  
- Kehrwert (1/x)  
- Potenz (xʸ)  
- Wurzel (√)  
- Vorzeichenwechsel (+/-)  

---

### Steuerung
- `=` Ergebnis berechnen  
- `⌫` letztes Zeichen löschen  
- `CE` aktuelle Zahl löschen  
- `C` alles löschen  

---

## Architektur (MVC)

**Model:**  
- Verantwortlich für die Berechnungslogik (`Calculator`)  

**View:**  
- Verantwortlich für die grafische Benutzeroberfläche (`gui_view.py`)  
- Zeigt Eingaben und Ergebnisse an  
- Enthält Buttons und Display  

**Controller:**  
- Steuert die Programmlogik (`Controller`)  
- Verarbeitet Eingaben aus der GUI  
- Verbindet View und Model  

---

## Komponenten

| Komponente   | Beschreibung |
|--------------|------------|
| `Calculator` | Mathematische Logik (add, subtract, multiply, divide, sqrt, power, etc.) |
| `View`       | GUI (Buttons, Display, Benutzerinteraktion) |
| `Controller` | Steuerung (Eingaben verarbeiten, Berechnung auslösen) |

---

## Datenfluss

Benutzer  
↓  
View (GUI)  
↓  
Controller  
↓  
Model (Calculator)  
↓  
Controller  
↓  
View  
↓  
Benutzer  

---

## Klassendesign

### Calculator (Model)
- `add(a, b)`  
- `subtract(a, b)`  
- `multiply(a, b)`  
- `divide(a, b)`  
- `sqrt(x)`  
- `power(a, b)`  
- `reciprocal(x)`  
- `percent(a, b)`  

---

### View (GUI)
-  

---

### Controller
- 

---

## Technologien
- Sprache: Python  
- GUI: Tkinter  
- Tools: VS Code, Python Interpreter  

---

## Scope
- Keine Klammern  
- Keine komplexen Funktionen (sin, log, etc.)  
- Keine Speicherfunktionen  
- Einfache GUI  
- Fokus auf Funktion, nicht Design  

---

## Edge Cases
- Division durch 0  
- Kehrwert von 0  
- Wurzel aus negativen Zahlen  
- Mehrere Operatoren hintereinander  
- Mehrere Dezimalpunkte in einer Zahl  
- Leere Eingabe bei `=`  
- Ungültige Eingaben  
- Sehr große oder sehr kleine Zahlen  

---

## Zukünftige Erweiterungen
- Speicherfunktionen (MC, MR, M+, M-)  
- Klammern  
- Verlaufsanzeige (History)  
- Tastatureingabe  
- Verbesserte GUI (Design)  
- Umwandlung in Desktop-App (.exe)  