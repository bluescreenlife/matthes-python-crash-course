from chapter_9_car import Car
from chapter_9_car import ElectricCar
from chapter_9_car import Battery

my_civic = Car("Honda", "Civic", 2011)
my_leaf = ElectricCar("Nissan", "Leaf", 2024)

print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()