import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    text = re.sub(r'^(.*?)\b([Aa]+)\b', r"\1argh", line)
    # print(text)
    text = re.sub(r'\b([a]+)\b', r"argh", line, 0, re.IGNORECASE) # 0 - не проверять повторы 
    print(text)

