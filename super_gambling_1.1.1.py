#super_gambling 1.1 SAVEFILE build
#TODO: Add way to delete savefile

#import Tkinter
import random
import os

#initialise global variables
balance = 2000 #money
name = ""
currency = "£"
save_loaded = False 

#define gambling
def gamble(bet=100):
    global balance
    if bet == 0:
        print("You bet nothing, you get nothing.")
    else:
        odds = {'☠️':0,'🍫':1,'🪙':2,'🍒':3,'🍍':4,'7':5} #'symbol':multiplier
        slot1,slot2,slot3 = random.choices(list(odds.items()),(9,45,30,15,5,1),k=3)
        balance -= bet
        print(f"You bet {currency}{bet} (Now holding {currency}{balance})")
        if slot1 == slot2 == slot3 or 0 in slot1 or 0 in slot2 or 0 in slot3: #if all slots are equal or there is a 0 in any position
            bet = bet*slot1[1]*slot2[1]*slot3[1]
        else:
            bet = bet*slot1[1] + bet*slot2[1] + bet*slot3[1]
        print(f"Slots: [{slot1[0]}][{slot2[0]}][{slot3[0]}]")
        balance += bet
        if bet:
            print(f"You won {currency}{bet}")
            print(f"Current Balance: {currency}{balance}")
        else:
            print("You won nothing. Better luck next time!")

#gameover
def gameover():
    print("Thanks for playing!")
    print("[Game Over, program will quit now]")
    os.system("PAUSE")
    quit()

#save file
def save():
    global name
    if not name:
        name = input("Enter savefile name: ")
    with open("savegamble.txt","w",encoding="utf-8") as file:
        file.write(f"{str(balance)}\n")
        file.write(f"{name}\n")
        file.write(f"{currency}")


#load file
def load():
    global balance
    global name
    global currency
    global save_loaded
    with open("savegamble.txt","r",encoding="utf-8") as file:
        balance = int(file.readline())
        name = file.readline()
        currency = file.readline()
    save_loaded = True
    

#settings
def settings():
    global currency
    sel = int(input("\n0 - Return to Menu\n1 - Change Currency Symbol\n"))
    match sel:
        case 0:
            menu()
        case 1:
            currency = input("Input new currency symbol:")
            print(f"New currency symbol: {currency}")
            settings()
        case _:
            settings()

    

#mode select
def menu():
    global balance
    global save_loaded
    try:
        file = open("savegamble.txt","r",encoding="utf-8")
    except:
        sel = int(input("\n0 - Settings\n1 - New Game\n------------\n3 - Quit\n"))
    else:
        file.close()
        sel = int(input("\n0 - Settings\n1 - New Game\n2 - Continue\n3 - Quit\n"))
    match sel:
        case 0:
            settings()
        case 1:
            game()
        case 2:
            try:
                load()
            except:
                print("Savefile corrupted or not found, please select 'New Game'")
                menu()
            else:
                sel = input(f"Load game of {name} with balance {currency}{balance}? Y/N: ")
                if sel == "Y":
                    game()
                else:
                    balance = 2000
                    save_loaded = False
                    menu()
        case 3:
            quit()
        case _:
            menu()

#runs at start
def main():
    quotes = ["“The only way I'll ever get hurt in the casino is if there's an earthquake and a slot machine falls on my foot.” - Jack Benny",
    "“If there weren’t luck involved, I would win every time.” - Phil Hellmuth",
    "“It’s not whether you won or lost, but how many bad beat stories you were able to tell.” - Grantland Rice",
    "“I’ve learned the lesson that the worst thing that can happen to a gambler is to let his recent losses or wins knock him off keel emotionally.” - Andrew Beter",
    "“When luck is on your side, it is not the time to be modest or timid. It is the time to go for the biggest success you can possibly achieve.” - Donald Trump",
    "“I've found that luck is quite predictable. If you want more luck, take more chances. Be more active. Show up more often.” - Brian Tracey",
    "“He who dares, wins!” - Del Boy",
    "“Money won is twice as sweet as money earned.” - 'Fast' Eddie Felson",
    "“At gambling, the deadly sin is to mistake bad play for bad luck.” - Ian Fleming",
    "“You don't gamble to win. You gamble so you can gamble the next day.” - Bert Ambrose",
    "“83%% of gamblers quit right before they would have hit the big one” - Journal of Financial Economics",
    "“keep gambling. borrow or steal money if you have to. you will make so much money” - @AlbertsStuff",
    "“One bad chapter doesn't mean your story is over. Keep gambling.” - @sloprules",
    "“I can't stop winning! - raxdflipnote”"]
    print(random.choice(quotes))
    menu()

#gameplay
def game():
    global balance
    if save_loaded:
        print(f"Welcome to Gamble, {name}")
    else:
        print("Welcome to Gamble.")
    print(f"You have {currency}{balance:,} in your bank account.")
    print("You could leave here empty handed, or you could leave here a millionaire. It all depends on how lucky you are.")
    gamestate = input("Are you ready to gamble? Y/N: ")
    if gamestate.upper() == "N":
        print("Looks like somebody else is going to hit the jackpot today.")
        gameover()
    while gamestate:
        print(f"\nYou have {currency}{balance:,}.")
        if balance == 0:
            print("You're broke!")
            print("Time to go home. Maybe your wife will believe you got mugged again?")
            gameover()
        try:
            stake = int(input("How much will you bet? "))
        except:
            stake = 0
        if stake > balance:
            print(f"Betting as much money as possible ({currency}{balance:,})")
            stake = balance
        gamble(stake)
        gamestate = input("Keep Gambling? Y/N: ")
        if gamestate.upper() == "N":
            print(f"\nYour Final Balance: {currency}{balance:,}")
            if balance <= 2000:
                print("Best to quit while you can still afford the train home.")
            elif balance >= 1000000:
                print("You madlad... you actually did it.")
            else:
                print("Nice Gambling!")
            yn = input("Save your balance and start where you left off next time? Y/N: ")
            if yn.upper() == "Y":
                save()
            gameover()

#program can be played as a game or used as a module            
if __name__ == "__main__":
    main()
