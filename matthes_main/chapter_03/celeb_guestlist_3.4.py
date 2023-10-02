import sys

if len(sys.argv) > 6:
    sys.exit

user = sys.argv[1]
celeb_guest_list = sys.argv[2:7]

def print_invites():
    for celeb in celeb_guest_list:
        print(f"Hello {celeb}, you are invited to {user}'s party.")

print_invites()

print(f"\nUnfortunately, {sys.argv[2]} is unable to attend.\n")

celeb_guest_list.remove(sys.argv[2])

print_invites()

print(f"\nGreat news, {user} got a bigger house. Let's invite some more celebs.\n")

celeb_guest_list.insert(0, "Gilmour")
celeb_guest_list.insert(3, "Rollins")

print_invites()

print(f"\nOops! The table is too small. We'll have to ask {celeb_guest_list[-1]} and {celeb_guest_list[-2]} to leave.\n")

kicked_guest1 = celeb_guest_list.pop(-1)
kicked_guest2 = celeb_guest_list.pop(-1)

print(f"\nByebye, {kicked_guest1} and {kicked_guest2}\n")

print_invites()