sandwich_orders = ["nebula", "bornk", "apollo", "beacon", "nebula", "comet candy", "boney billy",
                    "comet candy", "comet morehouse", "nebula", "disrupter", "apollo", "comet candy", "flash", "girf"]

finished_sandwiches = []
out_of_sandwiches = ["comet candy"]
    
for sammich in out_of_sandwiches:
    print(f"\nSorry, we are out of an ingredient today and cannot make the {sammich}.")
    while sammich in sandwich_orders:
        sandwich_orders.remove(sammich)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nNow making sandwich: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nSandwich prep complete. The following sandwiches are ready to go: ")
for sammich in finished_sandwiches:
    print(sammich)