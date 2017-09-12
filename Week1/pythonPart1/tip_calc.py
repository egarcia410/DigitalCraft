total = float(input('Total bill amount: '))
quality = input('Level of service (good, fair, bad): ').lower()

while True:
    quality = input('Level of service (good, fair, bad): ').lower()
    if quality == 'good':
        print(total * .20)
        break
    elif quality == 'fair':
        print(total * .15)
        break
    elif quality == 'bad':
        print(total * .10)
        break
