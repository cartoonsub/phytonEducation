
import sys
import re

# pattern = r'.*?cat.*?cat'
# for line in sys.stdin:
#     line = line.rstrip()
#     if not line:
#         break
#     if re.match(pattern, line):
#         print(line)

words = ['fuckcatcat', 'cat and cat cat',
         'catac', 'cat', 'ccatt', 'catFuckyoucat']
pattern = r'cat.*?cat'
for word in words:
    if re.search(pattern, word):
        print(word)
    print(re.search(pattern, word))
    print(re.findall('cat', word))


words = ['cat',
         'catapult and cat',
         'catcat',
         'concat',
         'Cat',
         '"cat"',
         '!cat?'
         ]
pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    if re.match(pattern, line):
        print(line)

pattern = r'(\w{2,})\1'
for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    if re.search(pattern, line):
        print(line)
