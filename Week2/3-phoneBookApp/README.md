# Write a Phone Book App

### Getting Started
1. Install [Python](https://www.python.org/downloads/)
2. Clone repository:

        git clone https://github.com/egarcia410/digitalCraft.git

3. Change directory:

        cd /digitalCraft/Week2/3-phoneBookApp

4. Run program:

        python3 index.py

You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:
```
$ python phonebook.py
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)?
```
1. If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
2. If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
3. If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
4. If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
5. If they choose to quit, end the program.
Example session:
```
$ python phonebook.py

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? 2
Name: Melissa
Phone Number: 584-394-5857
Entry stored for Melissa.

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? 2
Name: Igor
Phone Number: 857-485-2935
Entry stored for Igor.

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? 2
Name: Jazz
Phone Number: 334-584-2345
Entry stored for Jazz.

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? 1
Name: Melissa
Found entry for Melissa: 584-394-5857

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? 3
Name: Melissa
Deleted entry for Melissa

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? 4
Found entry for Igor: 857-485-2935
Found entry for Jazz: 334-584-2345

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? 5
Bye.
```
### Save the Database

The problem with the above program you've written is that all the information you've stored is lost the moment you exit the program. You will add the code necessary to save the database into a file. To save the file, you will provide an additional menu item: "Save entries".

When they choose to save entries, you save the dictionary that you are using to store all of the information into a file using the pickle module. Example code for saving a dictionary into a file:

*import json was used in this project

```
import pickle
...
# open the file in write mode (wb)
myfile = open('phonebook.pickle', 'wb')
# dump the contents of the phonebook_dict into myfile - the open file
pickle.dump(phonebook_dict, myfile)
# close myfile
myfile.close()
Restore the Saved Entries
```
Once you have the save entries feature implemented, you will need to restore the saved information at some point. Provide an additional menu item: "Load save entries" - which will load the saved dictionary from the previous saved file. To restore from a pickle file, use the pickle module to load the file:
```
# open the file in read mode (rb)
myfile = open('phonebook.pickle', 'rb')
# load the contents from the file and store it in the phonebook_dict variable
phonebook_dict = pickle.load(myfile)
```
Once you've completed the saving feature, you should be able to persist data over multiple runs of the program. Example session:
```
$ python phonebook2.py

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit
What do you want to do (1-7)? 2
Name: Melissa
Phone Number: 584-394-5857
Entry stored for Melissa.

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit
What do you want to do (1-7)? 2
Name: Igor
Phone Number: 857-485-2935
Entry stored for Igor.

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit
What do you want to do (1-7)? 2
Name: Jazz
Phone Number: 334-584-2345
Entry stored for Jazz.

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit
What do you want to do (1-7)? 4
Found entry for Melissa: 584-394-5857
Found entry for Igor: 857-485-2935
Found entry for Jazz: 334-584-2345

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit
What do you want to do (1-7)? 5
Entries saved to phonebook.pickle

1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit
What do you want to do (1-7)? 7
Bye.

$ python phonebook.py

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit
What do you want to do (1-7)? 6
Restored save entries.

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit
What do you want to do (1-7)? 4
Found entry for Melissa: 584-394-5857
Found entry for Igor: 857-485-2935
Found entry for Jazz: 334-584-2345
```
### Bonus Challenge

In addition to phone number, also support saving email and website URL for each entry. Hint: you will have to use nested dictionaries.