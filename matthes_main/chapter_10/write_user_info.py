from pathlib import Path
import json

def get_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for a new username, favorite band, and favorite type of beer."""
    username = input("What is your name? ")
    fav_band = input("What's your favorite band? ")
    fav_beer = input("What's your favorite type of beer? ")
    user_dict = {"username":username, "favorite band":fav_band, "favorite beer":fav_beer}
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user."""
    path = Path('/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_10/user_info.json')
    user_info = get_user_info(path)
    if user_info:
        correct_user = input(f"Information retrieved for user {user_info['username']}. Is this the correct user? (Y/N) ").lower()
        if correct_user == "y":
            print(f"Welcome back, {user_info['username']}! We've got the {user_info['favorite band']} queued up and a {user_info['favorite beer']} poured.")
        elif correct_user == "n":
            print("No problem. Let's get your info.")
            user_info = get_new_user_info(path)
            print(f"Great, we'll remember you next time, {user_info['username']}.")
        else:
            print("Input error.")

    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")

greet_user()