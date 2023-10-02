from pathlib import Path
import json

path = Path("favorite_number.json")

if path.exists():
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"I remember your favorite number. It's {fav_number}.")
else:
    fav_number = input("What's your favorite number? ")
    contents = json.dumps(fav_number)
    path.write_text(contents)