current_users = ["admin", "icenine", "greymachine", "marshmallow", "bluescreenlife91", "penelope.pup"]
new_users = ["iflondonburns", "abbottms", "Icenine", "Jjeyelashwishes", "Greymachine"]
new_users_lower = [item.lower() for item in new_users]

def main():
    if current_users == False:
        print("List of users is empty. Please add users and try again.")
    else:
        print(f"{len(current_users)} users exist.\n")

    for user in current_users:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?\n")
        else:
            print(f"Hello {user}, thank you for logging in.")
    
    for new in new_users_lower:
        if new in current_users:
            print(f"Sorry, username {new} has been taken. User not added.")
        else: 
            print(f"Username {new} is available. Welcome, {new}.")

if __name__ == "__main__":
    main()