# Base Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


# Regular Employee (fixed salary + bonus)
class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


# Contract Employee (hours * rate)
class ContractEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name, 0)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


# Manager (salary + allowance)
class Manager(Employee):
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance

    def calculate_salary(self):
        return self.salary + self.allowance


# ---- Testing Polymorphism ----
employees = [
    RegularEmployee("Javed", 30000, 5000),
    ContractEmployee("Satish", 100, 200),
    Manager("Rahul", 50000, 10000)
]

for emp in employees:
    print(emp.name, "Salary:", emp.calculate_salary())
