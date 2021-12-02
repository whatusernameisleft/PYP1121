student = {
    'name': '',
    'TP number': '',
    'marks': 0,
    'grade': '',
    'CGPA': 0.0
}

for info in student:
    student[info] = input(f'Please enter your {info}: ')

print('\nYour details are as follows:')

for info in student:
    print(f'{info[0].upper() + info[1:]}: {student[info]}')

print('Thank you for registering.')