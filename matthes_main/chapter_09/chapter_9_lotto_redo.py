from random import choice
from re import match

class Ticket:
    def __init__(self, length):
        self.code = []
        self.length = length
        code_etcher = 0
        char_bank = ["C", "O", "S", "M", "O", "1", "2", "3", "4", "5"]

        while code_etcher <= self.length:
            self.code.append(choice(char_bank))
            code_etcher += 1

    def __str__(self):
        return "".join(map(str, self.code))

def hit_jackpot(length):
    jackpot = Ticket(length)
    ticket = Ticket(length)
    count = 1  
        
    while str(ticket) != str(jackpot):
        print(f"\nWinning ticket: {jackpot}\nYour ticket: {ticket}")
        ticket = Ticket(length)
        count += 1
        print(f"Loser. Trying again: {count}")

    print(f"\nWINNER!\nJackpot: {jackpot}\nTicket: {ticket}\nNumber of tries: {count}")

hit_jackpot(3)