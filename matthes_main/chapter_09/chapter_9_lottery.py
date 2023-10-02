from random import choice

class Ticket:
    def __init__(self):
        self.code = []
        code_create = 0
        code_length = 0

        while code_create <= code_length:
            choices = ["L", 5, 2, "R", 3, "Z", 9, "E", "M", 1]
            self.code.append(choice(choices)) 
            code_create += 1
    
    def __str__(self):
        ticket = "".join(map(str, self.code))
        return ticket

class Lotto:
    def __init__(self):
        self.winning_code = []
        winning_code_create = 0
        winning_code_length = 0

        while winning_code_create <= winning_code_length:
            choices = ["L", 5, 2, "R", 3, "Z", 9, "E", "M", 1]
            self.winning_code.append(choice(choices)) 
            winning_code_create += 1

    def __str__(self):
        winning_ticket = "".join(map(str, self.winning_code))
        return winning_ticket

def hit_the_jackpot():
    jackpot = Lotto()
    winner = False
    attempt = 0

    while winner == False:
        new_ticket = Ticket()
        attempt += 1

        print(f"Attempt {attempt}:\nWinning ticket: {jackpot}\nYour ticket: {new_ticket}")
            
        if new_ticket == jackpot:
            winner = True
            print(f"Congats, you won the lottery after {attempt} tries!")

hit_the_jackpot()