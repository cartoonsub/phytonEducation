import sys
import re

pattern = r"\b(\w)(\w)"
words = ['this is a text', '"this\' !is. ?n1ce,']
for word in words:
    word = re.sub(pattern, r"\2\1", word)
    print(word)


import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    word = re.sub(pattern, r"\2\1", line)
    print(word)