from random import randint
from random import choice

class Die:
    def __init__(self, sides):
        self.sides = sides
        
    def roll_die(self, num_rolls):
        result_summary = []
        rolls_executed = 0

        while rolls_executed <= num_rolls:
            result_summary.append(randint(1, self.sides))
            rolls_executed += 1

        for result in result_summary:
            print(result)

d10 = Die(10)

d10.roll_die(5)
