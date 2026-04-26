# Analyse

## Benutzeranforderungen
- Benutzer kann Zahlen über Buttons eingeben (0–9)  
- Benutzer kann Dezimalzahlen eingeben (.)  
- Benutzer kann Rechenoperationen auswählen (+, -, ×, ÷)  
- Benutzer kann erweiterte Funktionen nutzen (% , 1/x, xʸ, √, +/-)  
- Benutzer kann Eingaben korrigieren (⌫, CE, C)  
- Benutzer kann das Ergebnis über `=` berechnen  
- Benutzer sieht die aktuelle Eingabe und das Ergebnis im Display  
- Benutzer erhält eine Fehlermeldung bei ungültigen Eingaben  

---

## Funktionale Anforderungen
- System muss Button-Eingaben verarbeiten  
- System muss mathematische Ausdrücke korrekt auswerten  
- System muss Grundrechenarten unterstützen (+, -, ×, ÷)  
- System muss erweiterte Funktionen korrekt berechnen:
  - Prozent (%)  
  - Kehrwert (1/x)  
  - Potenz (xʸ)  
  - Wurzel (√)  
  - Vorzeichenwechsel (+/-)  
- System muss Eingaben bearbeiten können:
  - ⌫ (ein Zeichen löschen)  
  - CE (aktuelle Zahl löschen)  
  - C (alles löschen)  
- System muss das Ergebnis im Display anzeigen  
- System muss Fehler erkennen und behandeln  

---

## Nicht-funktionale Anforderungen
- **Performance:** Berechnungen sollen sofort erfolgen (keine spürbare Verzögerung)  
- **Benutzerfreundlichkeit:** intuitive Bedienung über Buttons wie bei einem echten Taschenrechner  
- **Stabilität:** Programm darf bei falschen Eingaben nicht abstürzen  
- **Übersichtlichkeit:** klare Anzeige im Display  
- **Wartbarkeit:** Code soll strukturiert und erweiterbar sein  

---

## Edge Cases
- Division durch 0  
- Kehrwert von 0 (1/0)  
- Wurzel aus negativen Zahlen  
- Mehrere Operatoren hintereinander (z. B. ++, ×÷)  
- Mehrere Dezimalpunkte in einer Zahl (z. B. 3.1.4)  
- Leere Eingabe bei `=`  
- Ungültige Eingabesequenzen  
- Sehr große oder sehr kleine Zahlen  
- Prozent ohne gültigen Bezugswert  

---

## Technische Überlegungen
- Eingabe wird als String gespeichert (z. B. "12+5*3")  
- Verarbeitung erfolgt erst bei `=` oder speziellen Funktionen  
- Fehlerbehandlung muss zentral implementiert werden  
- GUI und Logik sollten getrennt aufgebaut sein  