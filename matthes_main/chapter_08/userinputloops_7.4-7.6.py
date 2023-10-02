## 7-4 pizza topping input loop -----------------------------------

# toppings = []

# while len(toppings) < 5:
#     toppings.append(input("\nEnter a topping to add to your pizza. Type 'quit' at any time to quit. Topping to add: "))
#     print(f"\nCurrent toppings list: ")
#     for topping in toppings:
#             print(topping)
#     if "quit" in toppings:
#             del toppings[-1]
#             break

# print(f"\nFinal toppings list: ")
# for topping in toppings:
#     print(topping)

## 7-5 movie tickets -----------------------------------
user_age = None

while user_age not in range(99):
    user_age = int(input("What's your age? "))
    if user_age < 3:
        print("Your ticket price is: free")
    elif 3 <= user_age <= 12:
        print("Your ticket price is: $10")
    elif user_age > 12:
        print("Your ticket price is: $15")
    else: 
        print("Please enter a number between 0 and 99.")
