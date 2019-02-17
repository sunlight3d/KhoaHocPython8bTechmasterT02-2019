class Person:
    base_salary = 10
    """Custom constructor"""
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.loginAttemps = 0
    def login(self):
        self.loginAttemps+=1
    def __repr__(self):
        return "Name = {}, email = {}, age = {}, loginAttemps = {}, base_salary={}"\
            .format(self.name, self.email, self.age, self.loginAttemps, self.base_salary)