#! python3

import re, pyperclip

##Todo
#Create Regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?        #area code (optional)
(\s|-)        #seperator
\d\d\d        #first three digits
-        #separator
\d\d\d\d        #last 4 digits
(((ext(\.)?\s)|x) #extension word part (optional)
 (\d{2,5}))?        #extension (optional)
)
''',re.VERBOSE)
#Create Regex for e-mail
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+ #Name part
@ #@ symbol
[a-zA-Z0-9_.+]+ #Domain name part
''',re.VERBOSE)
#Get the text off clipboard
text = pyperclip.paste()
##Get the e-mails
emails = emailRegex.findall(text)
print(emails)
##Get the phones
phones = phoneRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in phones:
    allPhoneNumbers.append(phoneNumber[0])
print(allPhoneNumbers)
results = '\n'.join(allPhoneNumbers) + '\n' + '\n' + '\n'.join(emails)
pyperclip.copy(results)