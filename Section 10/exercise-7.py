import re

namesRegex = re.compile(r'Agent (\w)\w*') ##Match Agent, a letter character followed by zero or more letter characters.
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

result = namesRegex.sub(r'Agent \1*****','Agent Alice gave the secret documents to Agent Bob.') ##First character is in group 1 and we are acessing it.
print(result)