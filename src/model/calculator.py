import math


class Calculator:
    """
    Reine Rechenlogik für den Taschenrechner.
    Enthält grundlegende und erweiterte mathematische Operationen.
    """

    # ---------------- GRUNDRECHENARTEN ----------------

    def add(self, a, b):
        """Addiert zwei Zahlen."""
        return a + b

    def subtract(self, a, b):
        """Subtrahiert b von a."""
        return a - b

    def multiply(self, a, b):
        """Multipliziert zwei Zahlen."""
        return a * b

    def divide(self, a, b):
        """
        Dividiert a durch b.

        Raises:
            ZeroDivisionError: Wenn b = 0 ist.
        """
        if b == 0:
            raise ZeroDivisionError("Nicht durch 0 Teilbar")
        return a / b

    # ---------------- ERWEITERTE FUNKTIONEN ----------------

    def power(self, a, b):
        """Berechnet a hoch b."""
        return a ** b

    def root(self, a):
        """
        Berechnet die Quadratwurzel von a.

        Raises:
            ValueError: Wenn a negativ ist.
        """
        if a < 0:
            raise ValueError("Ungültige Eingabe")
        return math.sqrt(a)

    def reciprocal(self, x):
        """
        Berechnet den Kehrwert (1/x).

        Raises:
            ZeroDivisionError: Wenn x = 0 ist.
        """
        if x == 0:
            raise ZeroDivisionError("Nicht durch 0 Teilbar")
        return 1 / x

    # ---------------- PROZENTRECHNUNG ----------------

    def percent(self, a, b, operator):
        """
        Führt Prozentrechnung abhängig vom Operator aus.

        Args:
            a (float): Basiswert
            b (float): Prozentwert
            operator (str): '+', '-', '*', '/'

        Returns:
            float: Ergebnis der Prozentrechnung

        Raises:
            ValueError: Bei ungültigem Operator
            ZeroDivisionError: Bei Division durch 0
        """

        if operator == "+":
            return a + (a * b / 100)

        elif operator == "-":
            return a - (a * b / 100)

        elif operator == "*":
            return a * (b / 100)

        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Nicht durch 0 Teilbar")
            return a / (b / 100)

        else:
            raise ValueError("Ungültiger Operator")