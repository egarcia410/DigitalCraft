
# Needs to be fixed, not accurate number of blue moons
def blueMoons():
    # Dictionary of key=Month and value=Number of days in each month
    daysInMonth = {
        '1': 31,
        '2': 28, # Every 4 years is a leap year
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31,
    }
    # Starting from first blue moon in year 2000
    month = '11'
    day = 30
    year = 2001
    numBlueMoons = 1

    while year < 2008:
        if year % 4 == 0: # Checks for leap years
            daysInMonth['2'] = 29
        else:
            daysInMonth['2'] = 28
        daysInPrevMonth = daysInMonth[month]
        currentDay = day + 29.5 # Blue Moon occurs every 29.5 days
        if currentDay > daysInPrevMonth: # Current day carries over into new month
            day = currentDay - daysInPrevMonth # Get day in new month
            intMonth = int(month) + 1 # Convert month to integer and increase by 1
            strMonth = str(intMonth) # Convert month back into a string
            month = strMonth # Set new month
            if intMonth > 12: # Starts a new year
                month = '1'
                year += 1
        else:
            day = currentDay
            print('INSIDE NUM OF BLUE MOONS')
            print('DAY', day)
            print('MONTH', month)
            print('YEAR', year)
            numBlueMoons += 1
            print('NUM BM = ', numBlueMoons)
        print('--------------------')
    return numBlueMoons
        
print(blueMoons())

