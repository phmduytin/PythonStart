class Employee:
    empCount = 0 #class data member
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.course = []
        Employee.empCount +=1

    def displayCount(self):
        print("Total: ", self.empCount)

    def displayEmployee(self):
        print("Name:{0}, Salary: {1}".format(self.name, self.salary))

    def enroll(self, course):
        self.course.append(course)

    def showEnrollCourse(self):
        print(self.course)

    @staticmethod
    def displayCount():
        print("Total: ", Employee.empCount)

Linh = Employee("Linh", 1000)
Ha = Employee("Ha", 800)

Employee.displayCount()

Linh.enroll("Math")
Linh.enroll("IT")
Linh.showEnrollCourse()

