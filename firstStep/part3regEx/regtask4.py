import sys
import re

pattern = r"(\w)\1{1,}"
words = ['attraction','buzzzz']
for word in words:
    word = re.sub(pattern, r"\1", word)
    print(word)

import sys
import re
pattern = r"(\w)\1{1,}"

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    word = re.sub(pattern, r"\1", word)
    print(word)