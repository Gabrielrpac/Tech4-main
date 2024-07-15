import locale

def format_number(number, format="%0.0f"):
    return locale.format_string(format, number, grouping=True)