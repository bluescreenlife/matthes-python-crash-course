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
