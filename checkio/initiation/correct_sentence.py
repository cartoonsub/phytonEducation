def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """

    letter = text[0].capitalize()
    result = letter + text[1:]
    if text[-1] != '.':
        result += '.'
    return result

print('Example:')
print(correct_sentence("welcome to New York"))

assert correct_sentence('greetings, friends') == 'Greetings, friends.'
assert correct_sentence('Greetings, friends') == 'Greetings, friends.'
assert correct_sentence('Greetings, friends.') == 'Greetings, friends.'
assert correct_sentence('greetings, friends.') == 'Greetings, friends.'

print("The mission is done! Click 'Check Solution' to earn rewards!")