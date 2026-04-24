import math

# als nächstes noch kehrwert 
# Kehrwert (Reziprokwert)

# Sie berechnet:

# 1/x

# Darstellung
# f(x) = 1/x
# 	​

# Beispiele
# 1/x von 2 → 1÷2=0,5
# 1/x von 4 → 1÷4=0,25
# 1/x von 0,5 → 1÷0,5=2

# Wichtig
# Bei 0 funktioniert das nicht 
# Division durch 0 ist nicht definiert


# Dann noch die Prozentrechnung mit einfügen 

# Typische Anwendungen
# 1. Rabatt berechnen 

# Beispiel:
# Ein Produkt kostet 100 €, Rabatt 20%

# Eingabe:

# 100 - 20 %

# Ergebnis: 80 €

# Der Rechner versteht:

# „Zieh 20% von 100 ab“

# 2. Aufschlag berechnen 

# Beispiel:
# 100 € + 19% MwSt

# Eingabe:

# 100 + 19 %

# Ergebnis: 119 €

# 3. Prozentwert berechnen

# Beispiel:
# Wie viel sind 20% von 50?

# Eingabe:

# 50 × 20 %

# Ergebnis: 10

# Wie der Rechner denkt

# Der %-Button bezieht sich immer auf die vorherige Zahl.

# Muster:

# A + B % → A + (B% von A)
# A - B % → A - (B% von A)
# A × B % → B% von A''


# modulo erstmal zur seite packen das kommt nicht in den normalen Standar-Rechner
 


class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b 
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b 

    def modulo(self, a, b):
        return a % b

    def potenz(self, a, b):
        return a ** b
    
    def root(self, a):
        return math.sqrt(a)


    