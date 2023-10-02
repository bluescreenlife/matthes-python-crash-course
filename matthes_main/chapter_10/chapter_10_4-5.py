from pathlib import Path

guest_list = Path("guest.txt")

write = True
names = ""

while write == True:
    new_guest = input("Enter the name to add to the guest list. Enter \"q\" at any time to quit.\nName to add: ")
    if new_guest == "q":
        write = False
    else:
        names += f"{new_guest}\n"

guest_list.write_text(names)

## read the file
read_guest_list = guest_list.read_text()
print("")
print(f"Guest list:\n{read_guest_list}")