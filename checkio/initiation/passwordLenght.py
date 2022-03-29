def is_acceptable_password(password: str) -> bool:
    if len(password) < 7:
        return False
    return True

    return bool(password[7::])


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('ashort0') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
