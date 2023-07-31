class Person:
    pname="vinay"
    def __init__(self, name, role):
        self.name=name
        self.role=role
    def details(self):
        return (self.name, self.role)
class People(Person):
    def __init__(self,name, role, number, email):
        self.number=number
        self.email=email
        Person.__init__(self,name,role)
    def show(self):
        return ("My name is {} and my email is {}".format(self.name, self.email))
class Peoples(People):
    def __init__(self, name, role, number, email, gender):
        self.gender=gender
        People.__init__(self,name, role, number, email)
    def speak(self):
        return ("My name is {} and my email is {} and my gender is {}".format(self.name, self.email, self.gender))

