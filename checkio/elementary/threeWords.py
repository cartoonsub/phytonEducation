import re

def checkio(words: str) -> bool:
    
    pattern = r"[a-z]+\s[a-z]+\s+[a-z]+"
    if re.search(pattern, words, re.IGNORECASE):
        return True
    return False

    # поиск в строке строк без чисел
    print("".join('dw'[w.isalpha()] for w in words.split()))
    checkio=lambda x:"www" in "".join('w' if w.isalpha() else 'd' for w in x.split())
    checkio=lambda x:"www" in "".join('dw'[w.isalpha()] for w in x.split())
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World 123 hello"))
    
    # assert checkio("Hello World hello") == True, "Hello"
    # assert checkio("He is 123 man") == False, "123 man"
    # assert checkio("1 2 3 4") == False, "Digits"
    # assert checkio("bla bla bla bla") == True, "Bla Bla"
    # assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
