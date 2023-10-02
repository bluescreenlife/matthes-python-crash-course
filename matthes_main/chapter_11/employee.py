class Employee:
    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def __str__(self):
        return f"{self.first.title()} {self.last.title()} is paid an annual salary of {self.annual_salary}"
    
    def give_raise(self, raise_amount = 5000):
        self.annual_salary += raise_amount