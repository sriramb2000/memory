from logic.game import *

if __name__ == "__main__":
    # 2 - 4 for now
    num_players = int(input("How many players?"))
    while num_players > 4 or num_players < 2:
        num_players = int(input("Please enter a number of players between 2 and 4: "))
    # Should be even number >= 2*numplayers
    num_cards = int(input("How many cards?"))
    while num_cards < 2*num_players or num_cards > 52 or num_cards%2 == 1:
        num_cards = int(input("Please enter an even number of cards greater or equal to twice the number of players and less than or equal to 52:"))
    # request player names
    playr_names = []
    for i in range(num_players):
        playr_names.append(input("Enter Player {}'s name: ".format(i+1)))

    game = Game(num_players, num_cards, playr_names)

    cur_player = 0
    while not game.is_over():
        game.display_game()
        print("It's {}'s turn".format(playr_names[cur_player]))
        #get valid input from player
        choice = int(input("Which card do you pick? ")) - 1
        while not game.is_valid_move(choice):
            choice = int(input("Please pick a valid card: ")) - 1
        #execute the move
        res = game.take_turn(cur_player, choice)
        if res == -1:
            print("Bad luck. Maybe next time.")
            cur_player += 1
            if cur_player >= num_players:
                cur_player = 0

    game.display_game()
    print("The winner is/are {}".format(game.get_winner()))
            
