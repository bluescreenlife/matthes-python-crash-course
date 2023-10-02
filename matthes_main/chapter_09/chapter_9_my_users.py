from users import User
from admin import Admin
from admin import Priveleges

andrew = Admin("Andrew", "VanderLeest", "5ft 8in", "175lb", "Guitar")
jenny = User("Jenny", "VanderLeest", "5ft 4in", "120lb", "Reading")

priveleges = Priveleges(andrew)

priveleges.show_priveleges()