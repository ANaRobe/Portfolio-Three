def intro():
    start_game()


def start_game():
    choice = input("Type in yes / no \n")
    if choice == "yes":
        round_one()
    else:
        game_over()


def round_one():
    # Choose protagonist
    choice = input("Type in young / old \n")
    if choice == "young":
        round_two()
    else:
        game_over()


def round_two():
    # Choose accesory
    choice = input("Type in horse / sword \n")
    if choice == "horse":
        round_three()
    else:
        game_over()


def round_three():
    # Choose partner
    choice = input("Type in sparrow / redman \n")
    if choice == "sparrow":
        round_four()
    else:
        game_over()


def round_four():
    # yes/no compromise
    choice = input("Type in yes / no \n")
    if choice == "yes":
        final_round()
    else:
        game_over()


def final_round():
    print("last challenge")


def game_over():
    print("GAME OVER")     


intro()           
