import re

digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')

print(mo.group()) ##This is greedy matching. It goes for the longest match choice.

digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')

print(mo.group()) ##This is non-greedy matching. It terminates at the first match..