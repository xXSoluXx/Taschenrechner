# Taschenrechner-V-0.1.0

## Beschreibung

Ein einfacher Konsolen-Taschenrechner zur Durchführung grundlegender mathematischer Operationen.
Das Projekt ist modular aufgebaut (MVC-Architektur), um spätere Erweiterungen wie GUI oder zusätzliche Funktionen zu ermöglichen.

---

## Ziel

Der Taschenrechner soll grundlegende mathematische Berechnungen durchführen können.
Der Nutzer kann Zahlen eingeben und einfache Rechenoperationen ausführen.

---

## Funktionen

* Addition, Subtraktion, Multiplikation und Division
* Eingabe von zwei Zahlen
* Auswahl der Rechenoperation
* Ausgabe des Ergebnisses
* Fehlerbehandlung (z. B. Division durch 0)

---

## Architektur (MVC)

### Model

Zuständig für die Logik (Berechnungen, Validierung)

### View

Zuständig für Ein- und Ausgabe (Konsole)

### Controller

Verbindet Model und View und steuert den Ablauf

---

## Komponenten

### Model

* Calculator
* Validation

### View

* Konsolenausgabe
* Eingabeaufforderung

### Controller

* Input Handling
* Programmlogik

---

## Datenfluss

Benutzer → View → Controller → Model → Controller → View

---

## Klassendesign

### Calculator

* add(a, b)
* subtract(a, b)
* multiply(a, b)
* divide(a, b)

### Controller

* handle_input()
* process_operation()

### View

* display_result()
* display_error()
* get_input()

---

## Technologien

* Sprache: Python 
* Framework: keiner (Konsolenanwendung)
* Tools: VS Code

---

## Scope

* Keine grafische Benutzeroberfläche (nur Konsole)
* Keine komplexen mathematischen Funktionen
* Keine Speicherung von Ergebnissen
* Keine Mehrfachberechnungen in einer Eingabe

---

## Edge Cases

* Division durch 0
* Ungültige Eingaben (Text statt Zahlen)
* Leere Eingaben
* Sehr große oder kleine Zahlen

---

## Mögliche zukünftige Erweiterungen

* GUI (z. B. mit Tkinter oder Qt)
* Prozentrechnung und Potenzen
* Verlauf (History) speichern
* Mehrere Berechnungen hintereinander
