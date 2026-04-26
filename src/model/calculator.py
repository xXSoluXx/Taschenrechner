import math


 
class Calculator:

    # Additions-berechnung 
    def add(self, a, b):
        return a + b
    
    # Subtraktions-berechnung
    def subtract(self, a, b):
        return a - b 
    
    # Multiplikations-berechnung 
    def multiply(self, a, b):
        return a * b
    
    # Division-berechnung
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Teilen durch 0 nicht möglich")
        return a / b  
    
    # Potenz-berechnung
    def power(self, a, b):
        return a ** b
    
    # Wurzel-berechnung
    def root(self, a):
        if a < 0:
            raise ValueError("Ungültige Eingabe")
        return math.sqrt(a)

    # Kehrwert-berechnung
    def reciprocal(self, x):
        if x == 0:
            raise ZeroDivisionError("Teilen durch 0 nicht möglich")
        return 1 / x

    # Prozent-berechnung
    def percent(self, a, b, operator):
        if operator == "+":
            return a + (a * b / 100)
        elif operator == "-":
            return a - (a * b / 100)
        elif operator == "*":
            return a * (b / 100)
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Teilen durch 0 nicht möglich")
            return a / (b / 100)
        else:
            raise ValueError("Ungültiger Operator")

    