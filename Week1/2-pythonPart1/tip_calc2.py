total = float(input('Total bill amount: '))
tip = 0
totalTip = total + tip

# Continues loop until correct level of service is entered
while True:
    quality = input('Level of service (good, fair, bad): ').lower()
    if quality == 'good':
        tip = total * .20
        break
    elif quality == 'fair':
        tip = total * .15
        break
    elif quality == 'bad':
        tip = total * .10
        break

numPeople = input('Split how many ways? ')
# Checks if input for numPeople is not a digit
while not numPeople.isdigit():
    numPeople = input('Split how many ways? ')


print('Tip amount: {}'.format(tip))
print('Total amount: ${}'.format(totalTip))
print('Amount per person: ${}'.format(totalTip / int(numPeople)))
