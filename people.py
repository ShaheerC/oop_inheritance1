class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hi my name is {}.".format(self.name)


class Student(Person):

    def learn(self):
        return"I get it!"


class Instructor(Person):

    def teach(self):
        return"An object is an instance of a class"

    
nadia = Instructor('Nadia')
print(nadia.greeting())

chris = Student('Chris')
print(chris.greeting())

print(nadia.teach())
print(chris.learn())

print(chris.teach())
#does not work because teach is an instance method for Instructor and not Student. If student was a child of instructor then this would work.