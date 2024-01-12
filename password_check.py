password = input()
def check_password(password: str) -> bool:
    if len(password) < 10:
        return False
    has_digit = False
    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True

    return has_lower and has_upper and has_digit
     


check_password(password)
