# Architektur

## Architektur: MVC

**Model:**
- Zuständig für Logik  

**View:**
- Zuständig für UI (hier: Konsole)  

**Controller:**
- Verbindet Model und View  

---

## Komponenten

**Model:**
- Calculator  
- Validation  

**View:**
- Konsolenausgabe  
- Eingabeaufforderung  

**Controller:**
- Input Handling  
- Steuerung der Programmlogik  

---

## Datenfluss
Benutzer → View → Controller → Model → Controller → View  

---

## Klassendesign (optional, aber sehr stark)

### Calculator
- add(a, b)  
- subtract(a, b)  
- multiply(a, b)  
- divide(a, b)  

### Controller
- handle_input()  
- process_operation()  
- run()

### View
- display_result()  
- display_error()  
- get_input()  
- get_operation()