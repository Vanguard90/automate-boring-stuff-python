import re

batRegex = re.compile(r'Bat(wo)?man') ##Question mark says group '(wo)' can appear in text once or 0 times.
mo = batRegex.search('The Advetures of Batman')

print(mo.group())