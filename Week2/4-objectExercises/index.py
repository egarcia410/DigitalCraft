# 1 Basics
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        return 'Hello {}, I am {}!'.format(other_person.name, self.name)

sonny = Person('Sonne', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)
