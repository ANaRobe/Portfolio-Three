import random
import sys
import time


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
    sprint("The story begins in ancient times... \n")
    sprint("There was Green Emperor, rulling over The Edge Of The World \n")
    sprint("He had only one daughter and no son to inherit his kingdom \n")
    sprint("His brother from The Other Edge Of The World had two boys... \n")
    sprint("Which one of them should cross the world to merry the princess?\n")
    start_game()


def spell_challenge():
    # Template where user can input words to break create an incantation phrase
    sprint("In order to escape he needs to say an Incantation \n")
    sprint("Lets help the prince with some words to break out the spell. \n")
    spell = input("Type in an incantation term \n").capitalize()
    feeling = input("Type in a feeling  \n")
    if spell == "":
        input("Please type in a word \n").lower()
    elif feeling == "":
        input("Please type in a word \n").lower()
    else:
        sprint(f"{spell}! Shall the {feeling} spirit make me human again!\n")
        sprint("Hey hey! Looking handsome again! \n")


def start_game():
    # Ask user if he wants to play
    sprint("Do you want to travel in time and join the Adventure? \n")
    while True:
        choice = input("Type in yes / no \n")
        if choice == "yes":
            round_one()
            continue
        elif choice == "no":
            sprint("Thanks for passing by! \n")
            game_over()
            play_again()
            continue
        else:
            sprint("Please, type in correctly! \n")


def round_one():
    # Choose protagonist
    sprint("Choose which one of the boys should cross the world to merry \n")
    while True:
        choice = input("Type in young / old \n")
        if choice == "young":
            round_two()
            continue
        elif choice == "old":
            sprint("After long journey he stopped to drink water \n")
            sprint("Oh no! He fell down in the well! \n")
            sprint("A scared magic frog transforms him in a fly to eat him \n")
            sprint("He escapes the well but as fly has only a day to live \n")
            spell_challenge()
            sprint("Dressed in a bear fur the king puts his son to test \n")
            sprint("But the prince is to frightened to fight\n")
            sprint("Crying like a baby is reutrning back home \n")
            game_over()
            play_again()
            continue
        else:
            sprint("Please, type in correctly! \n")


def round_two():
    # Choose accesory
    sprint("An old woman advices the young man \n")
    sprint("to ask his father for his Horse and his Sword \n")
    sprint("The king needs to protect his own kingdom and refuses \n")
    sprint("But eventually asks his son to choose between the two of them \n")
    while True:
        choice = input("Type in horse / sword \n").lower()
        if choice == "horse":
            round_three()
            continue
        elif choice == "sword":
            sprint("Dressed in a bear fur the king puts his son to test \n")
            sprint("The prince takes out his sword and fought \n")
            sprint("Unfortunately he is wounded and has to come back home..\n")
            game_over()
            play_again()
            continue
        else:
            sprint("Please, type in correctly! \n")


def round_three():
    sprint("Dressed in a bear fur the king puts his son to test \n")
    sprint("The horse is able to fly and escapes the confrontation \n")
    sprint("On the road he meets the Sparrow and the Redman \n")
    sprint("Which one of them should become the prince's slave? \n")
    while True:
        choice = input("Type in sparrow / redman \n").lower()
        if choice == "sparrow":
            round_four()
            continue
        elif choice == "redman":
            sprint("They wonder for long time and the prince gets hungry \n")
            sprint("Redman encourages him to steal some eggs from a farm \n")
            sprint("But an old wizard sees the boy in his garden \n")
            sprint("Instantly he transformes the prince into a pig \n")
            spell_challenge()
            sprint("But unforrtunately the boy was not able to speak again \n")
            sprint("and he came back home...")
            play_again()
            continue
        else:
            sprint("Please, type in correctly! \n")


def round_four():
    # yes/no compromise
    sprint("They wonder for long time and the Sparrow wins the boy's trust \n")
    sprint("Now he tricks the prince to go down to a well to cool off \n")
    sprint("To spare his life, the Sparrow forces him to obey him \n")
    sprint("Should the prince accept it? \n")
    while True:
        choice = input("Type in yes / no \n")
        if choice == "yes":
            guess_number()
            continue
        elif choice == "no":
            game_over()
            play_again()
            continue
        else:
            sprint("Please, type in correctly! \n")


def guess_number():
    # Generates a number between 1-3 and checks if it maches with user's input
    random_number = random.randint(1, 3)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and 3: \n"))
        if guess != random_number:
            sprint("You couldn't open the gates so you go back home \n")
            game_over()
            play_again()
            continue
        else:
            sprint("Congradulations! \n")
            sprint(f"You've guessed the number {random_number}! \n")
            level_two()
            continue
        break


def game_over():
    sprint("GAME OVER \n")


def level_two():
    sprint("The gates are opening... \n")
    sprint("Next level comig soon... \n")


def play_again():
    # Ask user if he wants to play again
    sprint("Do you want to play again? \n")
    while True:
        choice = input("Type in yes / no \n").lower()
        if choice == "yes":
            round_one()
            continue
        elif choice == "no":
            game_over()
            break
        else:
            sprint("Please, type in correctly! \n")


intro()
