class Controller:
    """
    Steuert die Verbindung zwischen GUI und Calculator-Logik.
    Parst Eingaben, führt Berechnungen aus und formatiert Ergebnisse.
    """

    def __init__(self, calculator):
        """Initialisiert den Controller mit einem Calculator-Objekt."""
        self.calc = calculator

    # ---------------- HAUPT-BERECHNUNG ----------------

    def calculate(self, expression):
        """
        Wertet einen einfachen mathematischen Ausdruck aus
        (z. B. '5+3', '10*2', '20%+5').

        Args:
            expression (str): Eingabe aus dem Display

        Returns:
            Ergebnis oder Fehlermeldung als String
        """
        try:
            # ---- Grundrechenarten erkennen ----
            for op in ["+", "-", "*", "/"]:
                if op in expression:

                    # Ausdruck teilen (z. B. "5+3" -> "5", "3")
                    a, b = expression.split(op)

                    # Dezimal-Komma in Punkt umwandeln
                    a = float(a.replace(",", "."))
                    b = float(b.replace(",", "."))

                    # ---- Prozentrechnung ----
                    if "%" in expression:
                        b = float(b.replace("%", "").replace(",", "."))
                        result = self.calc.percent(a, b, op)
                        return self.format_result(result)

                    # ---- Standardoperationen ----
                    if op == "+":
                        result = self.calc.add(a, b)
                        return self.format_result(result)

                    elif op == "-":
                        result = self.calc.subtract(a, b)
                        return self.format_result(result)

                    elif op == "*":
                        result = self.calc.multiply(a, b)
                        return self.format_result(result)

                    elif op == "/":
                        result = self.calc.divide(a, b)
                        return self.format_result(result)

            # Wenn kein Operator gefunden wurde
            raise ValueError("Ungültiger Ausdruck")

        # ---------------- FEHLERBEHANDLUNG ----------------
        except ZeroDivisionError:
            return "Kann nicht durch 0 teilen"

        except ValueError:
            return "Ungültige Eingabe"

        except Exception as e:
            print(e)  # Debug-Ausgabe
            return "Unbekannter Fehler"

    # ---------------- SPEZIALFUNKTIONEN ----------------

    def square(self, value):
        """Berechnet x²."""
        try:
            value = self.parse(value)
            result = self.calc.power(value, 2)
            return self.format_result(result)

        except ValueError:
            return "Ungültige Eingabe"

        except Exception:
            return "Error"

    def reciprocal(self, value):
        """Berechnet 1/x."""
        try:
            value = self.parse(value)
            result = self.calc.reciprocal(value)
            return self.format_result(result)

        except ZeroDivisionError:
            return "Division durch 0"

        except Exception:
            return "Error"

    def square_root(self, value):
        """Berechnet die Quadratwurzel von x."""
        try:
            value = self.parse(value)
            result = self.calc.root(value)
            return self.format_result(result)

        except ValueError:
            return "Keine Wurzel aus negativen Zahlen"

        except Exception:
            return "Error"

    # ---------------- HELFERFUNKTIONEN ----------------

    def format_result(self, result):
        """
        Formatiert Zahlen:
        - 5.0 → 5
        - 5.678 → 5.68
        """
        if isinstance(result, float) and result.is_integer():
            return int(result)

        return round(result, 2) if isinstance(result, float) else result

    def parse(self, value):
        """
        Wandelt String-Eingaben in float um
        (unterstützt Komma als Dezimaltrennzeichen).
        """
        return float(value.replace(",", "."))