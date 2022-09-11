import re

def first_word(text: str) -> str:
    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
    
    text = text.strip()

    result = text.split()
    return result[0]
    
    return re.search("([\w']+)", text).group(1)


print("Example:")
print(first_word(".greetings, friends"))

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
