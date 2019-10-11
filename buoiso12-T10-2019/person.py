class Person:
    """attributes = properties"""
    def __init__(self, name, age, job):
        print("This is a constructor")
        self.name = name
        self.age = age
        self.job = job
    """methods"""
    def walk(self):
        print("I am walking")
    def __str__(self):
        """__str__ is a toString method"""
        return "Name = "+self.name+"\n"\
                "Age = "+str(self.age)+"\n"\
                "Job = "+self.job
