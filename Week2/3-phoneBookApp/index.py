"""Phone Book App"""
import json

def phoneBook():
    """Phone Book App - Using JSON as a simple database for CRUD operation"""
    with open('temp.json', 'w') as f:
        json.dump({}, f)

    while True:
        print('\n')
        print('Electronic Phone Book')
        print('=====================')
        print('1. Look up an entry')
        print('2. Set an entry')
        print('3. Delete an entry')
        print('4. List all entries')
        print('5. Save entries')
        print('6. Restore saved entries')
        print('7. Quit')

        num = input('What do you want to do (1-5)? ')
        fname = 'temp.json'
        with open(fname, 'r') as f:
            data = json.load(f)
            if num == '1':
                searchEntry(data)
            elif num == '2':
                createEntry(data, fname)
            elif num == '3':
                deleteEntry(data, fname)
            elif num == '4':
                listEntries(data)
            elif num == '5':
                saveEntries(data)
            elif num == '6':
                restoreEntries(fname)
            elif num == '7':
                print('Bye')
                break

def searchEntry(data):
    """Search phone book for person by name"""
    name = input('Name: ')
    if name in data:
        print('Found entry for ' + name + ": " + data[name])
    else:
        print('Entry does not exist')

def createEntry(data, fname):
    """Create entry in phone book"""
    name = input('Name: ')
    phone = input('Phone Number: ')
    data[name] = phone
    with open(fname, 'w') as f:
        json.dump(data, f)
    print('Entry stored for ' + name)

def deleteEntry(data, fname):
    """Delete entry from phone book"""
    name = input('Name: ')
    if name in data:
        del data[name]
        with open(fname, 'w') as f:
            json.dump(data, f)
        print(name + " was deleted!")
    else:
        print('Name does not exist')

def listEntries(data):
    """Displays all entries in phone book"""
    if data:
        for name in data:
            print('\n')
            print('Name: ', name)
            print('Phone Number: ', data[name])
    else:
        print('No entries to display')

def saveEntries(data):
    """Save entries into data.json file"""
    with open('data.json', 'w') as f:
        json.dump(data, f)
    print('Entries saved to data.json')

def restoreEntries(fname):
    """Restore saved files from data.json"""
    with open('data.json', 'r') as f:
        with open(fname, 'w') as f1:
            for line in f:
                f1.write(line)
    print('Restored saved entries')

phoneBook()
