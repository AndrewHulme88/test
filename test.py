import random
import time

# define colors for the game
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#gangster business
gangster_business = ["Legal Consulting","Shadow Government Contracts","Arms Dealing","Protection Racket","Illegal Gambling","Drug Trafficking"]

#player info
player_cash = 100000
player_rank = 1

def display_cash():
    print(f"{color.BOLD}{color.GREEN}Cash:{color.END} ${player_cash}")

def display_rank():
    print(f"{color.BOLD}{color.YELLOW}Rank:{color.END} {player_rank}")

def game_intro():
    print(f"""{color.PURPLE}
 █▀ █▀█ ▄▀█ █▀   ▄▀█ █░ █▀▀ █░ █ █▀ 
 █▄ █▀▄ █▀█ ██▄   █▀█ █▄▄ ██▄ █▄ █ ██▄
{color.END}""")
    print(f"{color.BOLD}{color.RED}Welcome to the Gangster Business Simulator Game!{color.END}")
    print(f"You start with ${player_cash} and Rank: {player_rank}")

def get_user_input(options):
    while True:
        try:
            user_input = int(input("Enter a number(1-{}): ".format(len(options))))
            if user_input < 1 or user_input > len(options):
                print(f"{color.BOLD}{color.RED}Invalid input. Please choose a valid option.{color.END}")
            else:
                return user_input - 1
        except ValueError:
                print(f"{color.BOLD}{color.RED}Invalid input. Please enter a number.{color.END}")

def random_event():
    chance=random.randint(1,10)
    print(f"{color.BOLD}Random Event:{color.END} ",end=" ")
    if chance<=5:
        print("Nothing happens.")
    elif chance<=7:
        print(f"You were fined ${random.randint(1000,5000)} for a small operation gone wrong.")
        player_cash-=random.randint(1000,5000)
    elif chance<=8:
        print("You received a lucrative offer from a mysterious client. +$10,000")
        player_cash+=10000
    elif chance<=9:
        print(f"The police raided one of your hideouts. You lost ${random.randint(5000,15000)}")
        player_cash -= random.randint(5000,15000)
    else:
        print(f"A mysterious client offers you a big contract. Choose wisely. Your rank will increase by 1")
        player_rank+=1


def show_options(business_name):
    print(f"\n{color.BOLD}{color.BLUE}=={business_name}=={color.END}\n")
    print(f"{color.BOLD}1. Invest in this business{color.END}")
    print(f"{color.BOLD}2. Go to the next business opportunity{color.END}\n")

def business_opportunities():
    for i in range(len(gangster_business)):
        print(f"{color.BOLD}{i+1}.{color.END} {gangster_business[i]}")
    while True:
        user_choice = get_user_input(gangster_business)
        business_name=gangster_business[user_choice]
        #investing amount
        investing_amount=int(input(f"How much money do you want to invest in {business_name}($1000 - $100000): "))
        if investing_amount<1000 or investing_amount>100000:
            print(f"{color.BOLD}{color.RED}Invalid amount. Minimum investment is $1000 and Maximum is $100000.{color.END}")
        else:
            show_options(business_name)
            choice = get_user_input(["Invest", "Next Opportunity"])
            if choice == 0:
                profit = random.randint(int(investing_amount*0.1), int(investing_amount*2))
                print(f"{color.BOLD}{color.GREEN}You invested ${investing_amount} in {business_name} and earned ${profit} profit!{color.END}")
                player_cash += profit
                time.sleep(2)
            else:
                break
        random_event()
        display_cash()
        display_rank()

def main():
    game_intro()
    while True:
        business_opportunities()
        #user wants to exit the game
        restart=input("Want to play again?(y/n): ").lower()
        if restart =="n":
            break
        print(f"\n{color.BOLD}{color.YELLOW}Restarting the Game....{color.END}\n")
    print(f"{color.BOLD}{color.GREEN}Thanks for playing!{color.END}")

if __name__ == "__main__":
    main()
