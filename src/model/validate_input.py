def validate_input(value):
    """
    Prüft, ob value eine Zahl ist und >= 0.
    - Wenn keine Zahl, raise TypeError
    - Wenn negative Zahl, raise ValueError
    """
    # Komma zu Punkt umwandeln
    value = value.replace(",", ".")

    try:
        # Prüfen ob float notwendig ist
        if "." in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        raise TypeError("Nur Zahlen erlaubt!")
        
        