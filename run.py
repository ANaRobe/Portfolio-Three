def intro():
    start_game()


def spell_challenge():
    # Template where user can input words to break create an incantation phrase
    spell = input("Type in an incantation term \n").capitalize()
    feeling = input("Type in a feeling  \n")
    if spell == "":
        input("Please type in a word \n")
    elif feeling == "":
        input("Please type in a word \n")
    else:
        print(f"{spell}! Shall the {feeling} spirit make me human again!\n")


def start_game():
    choice = input("Type in yes / no \n")
    if choice == "yes":
        round_one()
    elif choice == "no":
        game_over()
    else:
        input("Please type in correctly: \n")


def round_one():
    # Choose protagonist
    choice = input("Type in young / old \n")
    if choice == "young":
        round_two()
    elif choice == "old":
        spell_challenge()
    else:
        input("Please type in correctly: \n")


def round_two():
    # Choose accesory
    choice = input("Type in horse / sword \n")
    if choice == "horse":
        round_three()
    elif choice == "sword":
        game_over()
    else:
        input("Please type in correctly: \n")


def round_three():
    # Choose partner
    choice = input("Type in sparrow / redman \n")
    if choice == "sparrow":
        round_four()
    elif choice == "redman":
        game_over()
    else:
        input("Please type in correctly: \n")


def round_four():
    # yes/no compromise
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
