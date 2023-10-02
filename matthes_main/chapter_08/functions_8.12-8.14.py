## 8.12 ---------------------------------------------------------------------------------

# def make_sandwich(meat, cheese, veggie, bread):
#     print(f"Sammich bot initializing. Creating a tasty sammich with: {meat}, {cheese} cheese, {veggie} on top, all snug in a {bread} bread hug.")

# def get_ingredients():
#     meat = input("Let's make a stellar sando. What type of meat do you want? ")
#     cheese = input("Now enter your cheese: ")
#     veggie = input("Enter a veggie: ")
#     bread = input("Finally, enter your bread: ")
#     return meat, cheese, veggie, bread

# if __name__ == "__main__":
#     meat, cheese, veggie, bread = get_ingredients()
#     make_sandwich(meat, cheese, veggie, bread)

## 8.13 ---------------------------------------------------------------------------------

# def build_profile(first, last, **user_info):
#     user_info["first name"] = first
#     user_info["last name"] = last
#     return user_info

# user_profile = build_profile("andrew", "vanderleest", location = "minneapolis", field = "nuthin")

# print(user_profile)

## 8.14 ---------------------------------------------------------------------------------

def make_car(make, model, **vehicle_info):
    vehicle_info["make"] = make
    vehicle_info["model"] = model
    return vehicle_info

car = make_car("honda", "civic", trim = "DX", stereo_upgrade = False)
print(car)