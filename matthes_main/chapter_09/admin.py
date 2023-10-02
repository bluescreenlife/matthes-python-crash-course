from users import User

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