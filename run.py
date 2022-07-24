import random
import sys
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def sprint(line):
    # Printing characters one by one
    for character in line:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == "\n":
            time.sleep(0.03)
        else:
            time.sleep(0.05)


def intro():
    print(f"""{Fore.YELLOW}


                       _    __    __    __    __    _                          
                      | |__|__|__|__|__|__|__|__|__|_|                         
 __    __    __       |_|___|___|___|___|___|___|___||       __    __    __   
|__|  |__|  |__|      |___|___|___|___|___|___|___|__|      |__|  |__|  |__|   
|__|__|__|__|__|       \____________________________/       |__|__|__|__|__|   
|_|___|___|___||        |_|___|___|___|___|___|___||        |_|___|___|___||
|___|___|___|__|        |___|___|___|___|___|___|__|        |___|___|___|__|   
 \_|__|__|___|/          \________________________/          \_|__|__|__|_/    
  \__|____|__/            |___|___|___|___|___|__|            \__|__|__|_/     
   |||_|_|_||             |_|___|___|___|___|__|_|             |_|_|_|_||      
   ||_|_|||_|__    __    _| _  __ |_ __  _ __  _ |_    __    __||_|_|_|_|      
   |_|_|_|_||__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|_|_|_|_||
   ||_|||_|||___|___|___|___|___|___|___|___|___|___|___|___|__||_|_|_|_|
   |_|_|_|_||_|___|___|___|___|___|___|___|___|___|___|___|___||_|_|_|_||
   ||_|_|_|_|___|___|___|___|___|___|___|___|___|___|___|___|__||_|_|_|_|
   |_|||_|_||_|___|___|___|___|___|___|___|___|___|___|___|___||_|_|_|_||
   ||_|_|_|_|___|___|___|___|___|_/| | | \__|___|___|___|___|__||_|_|_|_|
   |_|_|_|_||_|___|___|___|___|__/ | | | |\___|___|___|___|___||_|_|_|_||
   ||_|_|_|||___|___|___|___|___|| | | | | |____|___|___|___|__||_|_|_|_|
   |_|_|_|_||_|___|___|___|___|_|| | | | | |__|___|___|___|___||_|_|_|_||
  /___|___|__\__|___|___|___|___|| | | | | |____|___|___|___|_/_|___|__|_\ 
 |_|_|_|_|_|_||___|___|___|___|_|| | | | | |__|___|___|___|__|_|__|__|__|_|
 ||_|_|_|_|_|_|_|___|___|___|___||_|_|_|_|_|____|___|___|____|___|__|__|__|
    """)
    print("")
    print("")
    print(f"""{Fore.GREEN}
  _    _                                  _ _     
 | |  | |                           /\   | | |    
 | |__| | __ _ _ __ __ _ _ __      /  \  | | |__  
 |  __  |/ _` | '__/ _` | '_ \    / /\ \ | | '_ \ 
 | |  | | (_| | | | (_| | |_) |  / ____ \| | |_) |
 |_|  |_|\__,_|_|  \__,_| .__/  /_/    \_\_|_.__/ 
                        | |                       
                        |_|                                                                    
    """)
    print()    
    sprint("The story begins in ancient times... \n")
    sprint("There was Green Emperor, rulling over The Edge Of The World \n")
    sprint("He had only one daughter and no son to inherit his kingdom \n")
    sprint("His brother from The Other Edge Of The World had two boys... \n")
    start_game()


def spell_challenge():
    # Template where user can input words to break create an incantation phrase
    sprint("In order to escape he needs to say an Incantation \n")
    sprint("Lets help the prince with some words to break out the spell. \n")
    while True:
        spell = input(f"{Fore.BLUE}Type in a magic term \n").capitalize()
        feeling = input(f"{Fore.BLUE}Type in a feeling  \n").lower()
        if spell.strip() == "" or feeling.strip() == "":
            print(f"{Fore.RED}That doesn't break the spell \n")
            continue
        else:
            sprint(f"{spell}! Shall the {feeling} spirit make me human! \n")
            sprint("Hey hey! Looking handsome again! \n")
            break


def start_game():
    # Ask user if he wants to play
    sprint("Do you want to travel in time and join the Adventure? \n")
    while True:
        choice = input(f"{Fore.BLUE}Type in yes / no \n").lower().strip()
        if choice == "yes":
            round_one()
        elif choice == "no":
            sprint("Thanks for passing by! \n")
            game_over()
        else:
            print(f"{Fore.RED}Please, type in correctly! \n")
            continue


def round_one():
    # Choose protagonist
    sprint("Choose which one of the boys should cross the world to merry \n")
    while True:
        choice = input(f"{Fore.BLUE}Type in young / old \n").lower().strip()
        if choice == "young":
            round_two()
        elif choice == "old":
            sprint("After long journey he stopped to drink water \n")
            sprint("Oh no! He fell down in the well! \n")
            sprint("A scared magic frog transforms him in a fly to eat him \n")
            sprint("He escapes the well but as fly has only a day to live \n")
            spell_challenge()
            sprint("Dressed in a bear fur the king puts his son to test \n")
            sprint("But the prince is to frightened to fight\n")
            sprint("Crying like a baby is reutrning back home \n")
            play_again()
        else:
            print(f"{Fore.RED}Please, type in correctly! \n")
            continue


def round_two():
    # Choose accesory
    sprint("An old woman advices the young man \n")
    sprint("to ask his father for his Horse and his Sword \n")
    sprint("The king needs to protect his own kingdom and refuses \n")
    sprint("But eventually asks his son to choose between the two of them \n")
    while True:
        choice = input(f"{Fore.BLUE}Type in horse / sword \n").lower().strip()
        if choice == "horse":
            round_three()
        elif choice == "sword":
            sprint("Dressed in a bear fur the king puts his son to test \n")
            sprint("The prince takes out his sword and fought \n")
            sprint("Unfortunately he is wounded and has to come back home..\n")
            play_again()
        else:
            print(f"{Fore.RED}Please, type in correctly! \n")
            continue


def round_three():
    sprint("Dressed in a bear fur the king puts his son to test \n")
    sprint("The horse is able to fly and escapes the confrontation \n")
    sprint("On the road he meets the Sparrow and the Redman \n")
    sprint("Which one of them should become the prince's slave? \n")
    while True:
        choice = input(f"{Fore.BLUE}Type in sparrow / redman \n").lower()
        if choice.strip() == "sparrow":
            round_four()
        elif choice.strip() == "redman":
            sprint("They wonder for long time and the prince gets hungry \n")
            sprint("Redman encourages him to steal some eggs from a farm \n")
            sprint("But an old wizard sees the boy in his garden \n")
            sprint("Instantly he transformes the prince into a pig \n")
            spell_challenge()
            sprint("But unforrtunately the boy was not able to speak again \n")
            sprint("and he came back home... \n")
            play_again()
        else:
            print(f"{Fore.RED}Please, type in correctly! \n")
            continue


def round_four():
    # yes/no compromise
    sprint("They wonder for long time and the Sparrow wins the boy's trust \n")
    sprint("Now he tricks the prince to go down to a well to cool off \n")
    sprint("To spare his life, the Sparrow forces him to obey him \n")
    sprint("Should the prince accept it? \n")
    while True:
        choice = input(f"{Fore.BLUE}Type in yes / no \n").lower().strip()
        if choice == "yes":
            sprint("After 3 months crossing the mountains and the seas \n")
            sprint("he is finally in front of the kingdom's gate \n")
            sprint("To open it he need to guess a number between 1 and 3 \n")
            guess_number()
        elif choice == "no":
            play_again()
        else:
            print(f"{Fore.RED}Please, type in correctly! \n")
            continue


def guess_number():
    # Generates a number between 1-3 and checks if it maches with user's input
    random_number = random.randint(1, 3)
    guess = 0
    while guess != random_number:
        guess = int(input(f"{Fore.BLUE}Guess a number between 1 and 3: \n"))
        if guess != random_number:
            sprint("You couldn't open the gates so you go back home \n")
            play_again()
        else:
            sprint("Congradulations! \n")
            sprint(f"You've guessed the number {random_number}! \n")
            level_two()


def game_over():
    print(f"""{Fore.RED}
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                                                                    
    """)
    exit()


def level_two():
    print(f"{Fore.MAGENTA}The gates are opening... \n")
    print(F"{Fore.MAGENTA}Next level comig soon... \n")


def play_again():
    # Ask user if he wants to play again
    print(f"""{Fore.YELLOW}
 __     __           _               _   
 \ \   / /          | |             | |  
  \ \_/ /__  _   _  | |     ___  ___| |_ 
   \   / _ \| | | | | |    / _ \/ __| __|
    | | (_) | |_| | | |___| (_) \__ \ |_ 
    |_|\___/ \__,_| |______\___/|___/\__|
    """)
    sprint("Do you want to play again? \n")
    while True:
        choice = input("Type in yes / no \n").lower().strip()
        if choice == "yes":
            round_one()
        elif choice == "no":
            game_over()
        else:
            print(f"{Fore.RED}Please, type in correctly! \n")


intro()
