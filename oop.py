class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I'm a teacher!")

class Customer(User):
    # Creating the instance of the class:
    # __init__() is the constructor of the Customer class or the initiator
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    # Make a private property and it cannot be accessed if it is not set
    @property
    def name(self):
        # print("Getting the name")
        return self._name
    
    # Set the property to a certain value
    @name.setter
    def name(self, name):
        # print("Setting the name")
        self._name = name
        
    # Delete the class property
    @name.deleter
    def name(self):
        # print("Delete the class property")
        del self._name
            
    def update_membership(self, new_membership_type):
        # print("Updating the existing membership")
        self.membership_type = new_membership_type
        
    def __str__(self):
        return self.name + " " + self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer.name, customer.membership_type)
            
    # def __eq__(self, other):
        # if self.name == other.name and self.membership_type == other.membership_type
        #     return True
        # return False
        
    # __hash__ = None
    
    # __repr__ = __str__
        
users = [
        Customer("Liviu", "Bronze"),
        Customer("Andrei", "Silver"),
        Customer("Paul", "Gold"),
        Teacher()
    ]

for user in users:
    user.log()


# Customer.print_all_customers(customers)