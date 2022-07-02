
import re

# re.match
# re.search
# re.findall
# re.sub

# string = r'hello\nWorld'
# print(string)
# string = 'hello\nWorld'
# print(string)

pattern = r'abc'
pattern = r'a[abc]c'
string = 'bacccsss'
match_object = re.match(pattern, string)
# print(match_object)
match_object = re.search(pattern, string)
# print(match_object)

string = 'abc,s acc,s acc'
allInclusions = re.findall(pattern, string)
# print(allInclusions)

fixedTypos = re.sub(pattern, 'xyz', string)
# print(fixedTypos)

pattern = r'(abc)|(test|text)*'
string = 'testtext'
# allInclusions = re.findall(pattern, string)

matches = re.match(pattern, string)
# print(matches)
# print(matches.groups())
# print(matches.group(2))


pattern = r'(\w+)-\1'
string = 'abc-abd'
match = re.match(pattern, string, re.IGNORECASE)
print(match)

