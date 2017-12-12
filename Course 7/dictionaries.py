exam = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(exam['size'])


print(list(exam.keys()))

for k in exam.values():
    print(k)

for k, v in exam.items():
    print(k)
    print(v)