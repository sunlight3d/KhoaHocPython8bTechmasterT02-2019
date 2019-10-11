class Person:
    """attributes = properties"""
    def __init__(self, name, age, job):
        print("This is a constructor")
        self.name = name
        self.age = age
        self.job = job

    """instance method = created after constructor"""
    def walk(self):
        print("I am walking")
    def __str__(self):
        """__str__ is a toString method"""
        return "Name = "+self.name+"\n"\
                "Age = "+str(self.age)+"\n"\
                "Job = "+self.job
    @staticmethod
    def do_something():
        print("This is a static method")
