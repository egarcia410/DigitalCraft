# 1 Basics
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greet = []
        self.unique_count = 0

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
        if other_person not in self.unique_greet:
                self.unique_greet.append(other_person)
                self.unique_count += 1
        self.greeting_count += 1
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print('{0}\'s email: {1}, {0}\'s phone number: {2}'.format(self.name, self.email, self.phone))

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print(len(self.friends))

    def num_unique_people_greeted(self):
        print(self.unique_count)
        

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
dee_ann = Person('Dee Ann', 'deeAnn@gmail.com', '123-123-1234')

# sonny.greet(jordan)
# jordan.greet(sonny)

# print(sonny.email, sonny.phone)
# print(jordan.email, jordan.phone)

# ############################################################################
# 2 Make Your Own Class

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)


# car = Vehicle('Nissan', 'Leaf', 2015)
# car.print_info()

# sonny.print_contact_info()

# jordan.friends.append(sonny)
# sonny.friends.append(jordan)

# print(len(jordan.friends))

# jordan.add_friend(sonny)
# jordan.num_friends()

# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)

# print(jordan)

# ############################################################################
# Bonus Challenge
# Keep track of the number of unique people a person has greeted

sonny.num_unique_people_greeted()

sonny.greet(jordan)
sonny.num_unique_people_greeted()

sonny.greet(jordan)
sonny.num_unique_people_greeted()

sonny.greet(dee_ann)
sonny.num_unique_people_greeted()