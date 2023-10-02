people = [
    {
            "name:" : "Jenny",
            "sex:" : "yes please",
            "age:" : "33",
            "favorite color:" : "pink",
            "likes:" : "Andrew",
            "dislikes:" : "Andrew",
            "favorite beverage:" : "hazy IPA",
            "favorite pizza:" : "quatro fromaggi",
            "catch phrase:" : "Cosmo, NO!",
            "sibling:" : "Katie",
            "vehicle:" : "Toyota Rav4",
        }, 
    {
            "name:" : "Andrew",
            "sex:" : "male",
            "age:" : "too old for this",
            "favorite color:" : "I don't know, I'm not 7.",
            "likes:" : "dogs",
            "dislikes:" : "people",
            "favorite beverage:" : "free beer",
            "favorite pizza:" : "the one in front of me",
            "catch phrase:" : "serenity now",
            "sibling:" : "Allison",
            "vehicle:" : "Honda Civic"
        }
]

print(f"Who would you like to know about?\n")

for person in people:
    print(person["name:"])

active_person = ""

while active_person != ("Andrew" or "Jenny"):
    active_person = input("\nSelect person: ")
    if active_person == "Jenny":
        print("")
        for key, value in people[0].items(): 
            print(key, value)
    elif active_person == "Andrew":
        print("")
        for key, value in people[1].items():
            print(key, value)
    else:
        print("Please select a user from the list and try again.")