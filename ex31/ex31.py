class Employee:
    num_employees = 0

    def __init__(self, first, last, dept):
        Employee.num_employees += 1
        self.first = first
        self.last = last
        self.dept = dept
        self.email = first[0].lower() + last.lower() + "@warren.edu"
    def fullname(self):
        return f"{self.last}, {self.first}"

class Adjunct(Employee):
    def __init__(self, first, last, dept, rank):
        super().__init__(first, last, dept)
        self.rank = rank
        self.email = first.lower() + "." + last.lower() + "@warren.edu"

ADJ_DEPT = "Academics"
ADJ_SR = "Senior Adjunct"
ADJ_JR = "Adjunct"

emp1 = Employee("Steve", "Smith", "Faculty")
emp2 = Employee("Reimu", "Hakurei", "Youkai Extermination")
emp3 = Adjunct("Trevor", "Philips", ADJ_DEPT, ADJ_SR)
emp4 = Adjunct("Connie", "Maheswaran", ADJ_DEPT, ADJ_JR)

print(emp1.fullname(), emp1.dept)
print(emp2.fullname(), emp2.email)
print(emp3.fullname(), emp3.rank)
print(emp4.fullname(), emp4.email)

print("Total employees:", Employee.num_employees)