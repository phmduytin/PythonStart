#ịnh nghĩa một lớp gồm có tham số lớp và có cùng tham số instance

class Person:
    name = 'Person'
    def __init__(self, name = None):
        self.name = name

    def printPerSon(self):
        print(self.name)

t1 = Person()
t1.printPerSon()

print('%s name is %s' % (Person.name, t1.name))