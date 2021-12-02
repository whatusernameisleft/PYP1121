numList = []
total = 0.0

print('Input five numbers and you will get the average.')
for i in range(5):
    numList.append(float(input('Input a number: ')))

for num in numList:
    total += num

print(f'The average is: {total / 5}')