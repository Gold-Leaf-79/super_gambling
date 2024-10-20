#import Tkinter
import random
import os

#initialise variables
balance = 2000 #money
odds = {'☠️':0,'🍫':1,'🪙':2,'🍒':3,'🍍':4,'7':5} #'symbol':multiplier
name = ""

#define gambling
def gamble(cash, bet=100):
    slot1,slot2,slot3 = random.choices(list(odds.items()),(3,45,30,15,5,1),k=3)
    cash -= bet
    bet = bet*slot1[1]*slot2[1]*slot3[1]
    print(f"Slots: [{slot1[0]}][{slot2[0]}][{slot3[0]}]")
    cash += bet
    print(f"You won £{bet}")
    return cash

#gameover
def gameover():
    print("[Game Over, program will quit now]")
    os.system("PAUSE")
    quit()

#gameplay
print("Welcome to the slot machine.")
print(f"You have £{balance:,} in your pocket.")
print("You could leave here empty handed, or you could leave here a millionaire. It all depends on how lucky you are.")
gamestate = input("Are you ready to gamble? Y/N: ")
if gamestate == "N":
    print("Looks like somebody else is going to hit the jackpot today.")
    gameover()
while gamestate:
    print(f"Current balance: {balance:,}")
    if balance == 0:
        print("You're broke!")
        print("Time to go home. Maybe your wife will believe you got mugged again?")
    stake = int(input("How much will you bet? "))
    if stake > balance:
        print(f"Betting as much money as possible (£{balance:,})")
        stake = balance
    balance = gamble(balance,stake)
    gamestate = input("Keep Gambling? Y/N: ")
    if gamestate == "N":
        print(f"Your Final Balance: £{balance:,}")
        if balance <= 2000:
            print("Best to quit while you can still afford the train home.")
        elif balance >= 1000000:
            print("You madlad... you actually did it.")
        else:
            print("Nice Gambling!")
        gameover()