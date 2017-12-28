import re #support for regular expressions

message = 'Call me at 0638110739 or you can also call me tomorrow at 0644319624'

phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d') ##We're looking for this pattern of text and we will store it as a regular expression object in this variable.
##match = phoneNumRegex.search(message) ###Find the first match
##print(match.group()) 

print(phoneNumRegex.findall(message))