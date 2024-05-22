
import re
text = input()

# text = "A man, a plan, a canal: Panama"

text = re.sub(r'[^a-zA-Z0-9]', '', text)
text = text.strip().lower()

if text == text[::-1]:
    print(True)
else:
    print(False)
