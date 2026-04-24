
# Eingabe formatieren je nachdem ob der Nutzer ein int oder float eingibt 
def format_result(result):
    if isinstance(result, float):
        if result.is_integer():
            return int(result)
        else:
            return round(result, 2)
    return result