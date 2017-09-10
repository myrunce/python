# declare a class and give it name User
class User(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables. just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help a user login
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
        
#now create an instance of the class
new_user = User("Anna","anna@anna.com")
print new_user.email

#To review:
#A class: Instructions for how to build many objects that share characteristics.
#An object: A data type built according to specifications provided by the class definition.
#An attribute: A value. Think of an attribute as a variable that is stored within an object.
#A method: A set of instructions. Methods are functions that are associated with an object. 
#Any function included in the parent class definition can be called by an object of that class.
