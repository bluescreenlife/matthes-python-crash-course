class Restaurant:
    def __init__(self, name, cuisine, number_served):
        self.name = name
        self.cuisine = cuisine
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine} cuisine. It has served {self.number_served} customers.")

    def open_restaurant(self):
        print(f"{self.name} is open for business.")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served

    def order_burger(self, num_burgers):
        self.number_served += num_burgers
        print(f"Order placed. Your order is order no. {self.number_served}")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, number_served, flavors):
        super().__init__(name, cuisine, number_served)
        self.flavors = flavors


    def get_flavors(self):
        print(f"Here at {self.name}'s ice cream shoppe, we offer the following flavors:\n")
        for flavor in self.flavors: print(flavor)

class User:
    def __init__(self, first_name, last_name, height, weight, hobby):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.height = height
        self.weight = weight
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.height} tall, and weighs {self.weight} lbs. {self.first_name}'s hobby is {self.hobby}.")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self, num):
        self.login_attempts += num

    def reset_logn_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, height, weight, hobby):
        super().__init__(first_name, last_name, height, weight, hobby)
        self.priveleges = Priveleges(self)

class Priveleges:
    def __init__(self, priveleges):
        priveleges = ["can add post", "can delete post", "can ban user", "can mute user", "can add user"]
        self.priveleges = priveleges
        
    def show_priveleges(self):
        for privelege in self.priveleges:
            print(privelege)


vandys = Restaurant("Vandy's", "American", 25)
sandys = Restaurant("Sandy's", "African", 15)
randys = Restaurant("Randy's", "Chinese", 5)

flavors = ["vanilla", "chocolate", "strawberry", "rasberry", "banana", "tuti fruity"]

dandys = IceCreamStand("Dandy's", "Ice Cream", 117, flavors)

andrew = User("andrew", "vanderleest", "5ft 8in", "175lb", "playing guitar")
jenny = User("jenny", "vanderleest", "5ft 4in", "120lb", "le arts")
marshall = User("marshall", "vanderleest", "smol", "17lb", "eating tags")

user_list = [andrew, jenny, marshall]

admin = Admin("Andrew", "VanderLeest", "5ft 8in", "175lb", "playing guitar")
admin.priveleges.show_priveleges()