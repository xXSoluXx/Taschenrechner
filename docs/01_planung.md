# 🧮 Projekt: Taschenrechner V.0.1.0 (mit erweiterten Grundfunktionen)

## 🎯 Ziel
Der Taschenrechner soll wie ein klassischer Taschenrechner funktionieren und grundlegende mathematische Berechnungen über eine Button-basierte GUI ermöglichen.

---

## Hauptfunktionen

### Eingabe
- Zahlen (0–9)  
- Dezimalzahlen (.)  

---

### Rechenoperationen
- Addition  
- Subtraktion  
- Multiplikation  
- Division  

---

## Erweiterte Funktionen

### Gleichheits-Taste (=)
Berechnet den gesamten eingegebenen Ausdruck und zeigt das Ergebnis an:

- 12 + 5 × 2 = 22  
- 10 ÷ 2 = 5  

---

### Prozent (%)
Funktion wie im normalen Taschenrechner:

- A + B % → A + (B% von A)  
- A - B % → A - (B% von A)  
- A × B % → B% von A  

---

### 🔁 Kehrwert (1/x)
Berechnet den Reziprokwert:

**Beispiele:**
- 4 → 0.25  
- 0.5 → 2  

Fehlernrehandlung:
- Division durch 0 abfangen (Ungültige Eingabe)  

---

### Potenz (xʸ)
- 2^3 → 8  
- 5^2 → 25  

---

### Wurzel (√x)
- √9 → 3  
- √16 → 4  

Fehler:
- Ungültige Eingabe keine negativen Zahlen  

---

### Vorzeichen wechseln (+/-)
- 5 → -5  
- -3 → 3  
- 12 + 5 → 12 + (-5)  

---

### Alles löschen (C)
- löscht komplette Eingabe  
- setzt Ausdruck zurück  
- Ergebnis wird gelöscht  

---

### Aktuelle Eingabe löschen (CE)
- löscht nur die aktuelle Zahl  

**Beispiele:**
- 12 + 345 → CE → 12 +  
- 50 × 9 → CE → 50 ×  

---

### Backspace
Löscht das letzte Zeichen:

- 123 → 12  
- 45+6 → 45+  

---

### Dezimalpunkt (.)
- 3.14  
- 0.5  
- 10.0  

---

## Tastenfunktionen

- [+] Addition  
- [-] Subtraktion  
- [×] Multiplikation  
- [÷] Division  
- [=] Ergebnis berechnen  
- [.] Dezimalpunkt  
- [x²] Potenz  
- [%] Prozentrechnung  
- [√] Quadratwurzel  
- [1/x] Kehrwert  
- [+/-] Vorzeichen wechseln  
- [⌫] letztes Zeichen löschen  
- [C] alles löschen  
- [CE] aktuelle Zahl löschen  

---

## Benutzeroberfläche (GUI)

### Display
- zeigt aktuelle Eingabe und Ergebnis  

---

### Button-Layout


  %  CE C ⌫
1/x  xʸ √  ÷
  7  8  9  ×
  4  5  6  -
  1  2  3  +
+/-  0  .  =


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