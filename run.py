def intro():
    print("The story begins in ancient times... \n")
    print("There was Green Emperor, rulling over The Edge Of The World \n")
    print("He had only one daughter and no son to inherit his kingdom \n")
    print("His brother from The Other Edge Of The World had two boys... \n")
    print("Which one of them should cross the world to merry the princess?\n")
    start_game()


def spell_challenge():
    # Template where user can input words to break create an incantation phrase
    print("In order to escape he needs to say an Incantation \n")
    print("Lets help the prince with some words to break out the spell.")
    spell = input("Type in an incantation term \n").capitalize()
    feeling = input("Type in a feeling  \n")
    if spell == "":
        input("Please type in a word \n")
    elif feeling == "":
        input("Please type in a word \n")
    else:
        print(f"{spell}! Shall the {feeling} spirit make me human again!\n")
        print("Hey hey! Looking handsome again! \n")


def start_game():
    # ask user if he wants to play
    print("Do you want to travel in time and join the Adventure? \n")
    choice = input("Type in yes / no \n")
    if choice == "yes":
        round_one()
    elif choice == "no":
        print("Thanks for passing by! \n")
        game_over()
    else:
        input("Please type in correctly: \n")


def round_one():
    # Choose protagonist
    print("Choose which one of the boys should cross the world to merry \n")
    choice = input("Type in young / old \n")
    if choice == "young":
        round_two()
    elif choice == "old":
        print("After long journey he stopped to drink water \n")
        print("Oh no! He fell down in the well! \n")
        print("A scared magic frog transforms him in a fly to eat him \n")
        print("He escapes the well but as fly has only one day to live \n")
        spell_challenge()
        print("Dressed in a bear fur the king puts his son to test \n")
        print("But the prince is to frightened to fight\n")
        print("now he is running back to the castle crying like a baby \n")
        game_over()
    else:
        input("Please type in correctly: \n")


def round_two():
    # Choose accesory
    print("An old woman advices the young man \n")
    print("to ask his father for his Horse and his Sword \n")
    print("The king needs to protect his own kingdom and refuses \n")
    print("But eventually asks his son to choose between the two of them \n")
    choice = input("Type in horse / sword \n")
    if choice == "horse":
        round_three()
    elif choice == "sword":
        print("Dressed in a bear fur the king puts his son to test \n")
        print("The prince takes out his sword and fought \n")
        print("Unfortunately he is wounded and has to come back home...\n")
        game_over()
    else:
        input("Please type in correctly: \n")


def round_three():
    print("Dressed in a bear fur the king put his son to test \n")
    print("The horse is able to fly and escapes the confrontation \n")
    print("On the road he meets the Sparrow and the Redman \n")
    print("Which one of them should become the prince's slave? \n")
    choice = input("Type in sparrow / redman \n")
    if choice == "sparrow":
        round_four()
    elif choice == "redman":
        game_over()
    else:
        input("Please type in correctly: \n")


def round_four():
    # yes/no compromise
    print("They wonder for long time and the Sparrow wins the boy's trust \n")
    print("Now he tricks the prince to go down to a well to cool off \n")
    print("To spare his life, the Sparrow forces him to obey him \n")
    print("Should the prince accept? \n")
    choice = input("Type in yes / no \n")
    if choice == "yes":
        final_round()
    elif choice == "no":
        game_over()
    else:
        input("Please type in correctly: \n")


def final_round():
    print("last challenge")


def game_over():
    print("GAME OVER")


intro()
