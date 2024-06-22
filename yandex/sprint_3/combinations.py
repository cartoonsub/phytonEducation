
class Combinators():
    def __init__(self) -> None:
        self.allPosibilities = []


    def getCombinations(self, keys: list) -> str:
        buttons = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }

        lettersList = []
        for key in keys:
            lettersList.append(buttons[key])

        self.setPosibilities(lettersList)
        return ' '.join(self.allPosibilities).strip()

    def setPosibilities(self, lettersList, text='', limit=0) -> str:
        if limit > len(lettersList) - 1:
            self.allPosibilities.append(text)
            return ''

        for letter in lettersList[limit]:
            self.setPosibilities(lettersList, text + letter, limit + 1) + ' '
        return text


input = input()
input = list(int(i) for i in input)

combinators = Combinators()
print(combinators.getCombinations(input))
