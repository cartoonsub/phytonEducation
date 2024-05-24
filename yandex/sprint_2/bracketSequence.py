
def main():
    text = str(input())
    if not text:
        print(True)
        return
    first_symbol = text[0]
    last_symbol = text[-1]
    match last_symbol:
        case '{':
            print(False)
            return
        case '(':
            print(False)
            return
        case '[':
            print(False)
            return
    
    match first_symbol:
        case '}':
            print(False)
            return
        case ')':
            print(False)
            return
        case ']':
            print(False)
            return

    stack = []
    for symbol in text:
        if symbol == '{' or symbol == '(' or symbol == '[':
            stack.append(symbol)
            continue
        
        if not stack:
            print(False)
            return
        last_symbol = stack.pop()
        if symbol == '}' and last_symbol != '{':
            print(False)
            return
        if symbol == ')' and last_symbol != '(':
            print(False)
            return
        if symbol == ']' and last_symbol != '[':
            print(False)
            return
    
    if stack:
        print(False)
        return
    print(True)

if __name__ == '__main__':
    main()
