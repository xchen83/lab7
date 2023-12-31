from logic import Game, Human, Bot

if __name__ == '__main__':
    num_players = Game()

    game = Game()
    human_player = Human()

    if num_players == 1:
        bot_player = Bot()
    else:
        bot_player = Human()

    print("Welcome to Tic-Tac-Toe!")

    while not game.leaveLoop:
        if game.turnCounter % 2 == 0:
            game.print_board()
            number_picked = human_player.make_move()
            if 1 <= number_picked <= 9:
                game.modify_array(number_picked)
                game.other_player()
                game.print_board()
            else:
                print("Invalid input. Please try again.")
            game.turnCounter += 1
        else:
            other_player_choice = bot_player.make_move() if num_players == 1 else human_player.make_move()
            print("\nOther Player's Choice:", other_player_choice)
            game.modify_array(other_player_choice)
            game.other_player()
            game.turnCounter += 1

        winner = game.get_winner()
        if winner != "N":
            game.print_board()
            print(f"{winner} won!")
            break
        elif game.turnCounter == 9:
            game.print_board()
            print("It's a draw!")
            break
