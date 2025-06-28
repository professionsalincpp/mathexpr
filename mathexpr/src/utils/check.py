# Checkers

def check_is_number(char: str) -> bool:
    if char is None:
        return False
    return char.isdigit() or char == '.'

def check_is_identifier(char: str) -> bool:
    if char is None:
        return False
    return (char.isalpha() or char.isdigit() or char == '_') and char not in ['(', ')', '[', ']', '{', '}', ';']