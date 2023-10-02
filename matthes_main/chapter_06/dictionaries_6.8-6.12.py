pets = [
    {
        "name" : "penelope",
        "owner name" : "andrew",
        "species" : "dog",
        "breed" : "boston terrier",
        "attitude" : "driven",
        "favorite activities" : ["fetch", "jump", "run", "dig"]
    },
    {
        "name" : "cosmo",
        "owner name" : "jenny",
        "species" : "dog",
        "breed" : "boston terrier",
        "attitude" : "lazy",
        "favorite activities" : "blanket"
    },
    {
        "name" : "rona",
        "owner name" : "erin",
        "species" : "cat",
        "breed" : "do cat breeds matter?",
        "attitude" : "security guard",
        "favorite activities" : ["eating", "sleeping", "creeping"]
    },
    {
        "name" : "cici",
        "owner name" : "michael",
        "species" : "cat",
        "breed" : "do cat breeds matter?",
        "attitude" : "lassiez-faire",
        "favorite activities" : "stalk"
    }
]

for pet in pets:
    print("")
    for key, value in pet.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"{item}")
        else:
            print(f"{key}: {value}")
