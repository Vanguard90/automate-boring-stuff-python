import re

name = 'First Name: Enes Last Name: Kirimi'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
result = nameRegex.findall(name)
print(result)