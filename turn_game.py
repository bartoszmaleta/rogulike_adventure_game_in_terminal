 # Turn Based Battle Simulator

# Player and boss take turns to attack each other with different moves
# until one is defeated.
import ui as ui
import engine as engine
import random
import helpers as helpers


def wizard(character_type):
    
    return wizard


def how_to_play():
    """Main function that will welcome the player to the game."""

    print("\tWelcome to Battle Sim! This is a turn based combat simulator where")
    print("\tthere can only be one winner.")

    print("\nHow to play.\n\nPlayers take turn to choose a move. Moves can either deal moderate damage")
    print("with a low range, deal high damage but over a wide")
    print("range, or they can heal. (Note: Moves can miss, including Heal!)")

    print("\nEach player starts with 100 health, and the first")
    print("player to reduce their opponent to 0 is the winner.")

    print("\nThat's it! Good luck")
    

def fighting_boss(character_type, health_of_player_in_the_whole_game):
    # print(character_type)

    # """Main function that will welcome the player to the game."""

    # print("\tWelcome to Battle Sim! This is a turn based combat simulator where")
    # print("\tthere can only be one winner.")

    # print("\nHow to play.\n\nPlayers take turn to choose a move. Moves can either deal moderate damage")
    # print("with a low range, deal high damage but over a wide")
    # print("range, or they can heal. (Note: Moves can miss, including Heal!)")

    # print("\nEach player starts with 100 health, and the first")
    # print("player to reduce their opponent to 0 is the winner.")

    # print("\nThat's it! Good luck")

    play_again = True

    # Set up the play again loop
    while play_again:

        winner = None
        player_health = 100
        boss_health = 100

        # determine whose turn it is
        turn = random.randint(1, 2)  # heads or tails
        if turn == 1:
            helpers.clear_screen()
            player_turn = True
            boss_turn = False
            print("\nPlayer will attack first.")
            ui.blank_line()
        else:
            player_turn = False
            boss_turn = True
            print("\nBoss will attack first.")
            ui.blank_line()

        print("PLAYER HEALTH ", player_health)
        print("BOSS HEALTH: ", boss_health)

        # set up the main game loop
        while (player_health != 0 or boss_health != 0):
            # ui.display_assassin_and_alien_boss(fight_graphic)
            ui.display_fight(character_type)
            heal_up = False  # determine if heal has been used by the player. Resets false each loop.
            miss = False  # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            # moves = {"Deadpunch": random.randint(18, 25),
            #          "Fireball": random.randint(10, 35),
            #          "Heal": random.randint(20, 25)}
            
            if character_type == "wizard":
                moves = {"Fireball": random.randint(18, 25),
                         "Spell of destruction": random.randint(10, 35),
                         "Heal": random.randint(20, 25)}
            elif character_type == "warrior":
                moves = {"Sword spike": random.randint(18, 25),
                         "Deadpunch": random.randint(10, 35),
                         "Heal": random.randint(20, 25)}

            elif character_type == "assassin":
                moves = {"Poisonous dagger spike": random.randint(18, 25),
                         "Rain of death": random.randint(10, 35),
                         "Heal": random.randint(20, 25)}

            computer_moves = {"Toxic Bite": random.randint(5, 10),
                              "Furious ultra mega rage attakck": random.randint(5, 10),
                              "Heal": random.randint(10, 15)}   

            # Should be this one working, but commented to make sure we win!
            # computer_moves = {"Toxic Bite": random.randint(18, 25),
                            #   "Furious ultra mega rage attakck": random.randint(10, 35),
                            #   "Heal": random.randint(20, 25)}         
        
            print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            # print(character_type)

            if player_turn:
                print('----------------- YOUR TURN -----------------------------------------------------------------------------------------------------------------------------------------')
                first_element_of_moves_dict = list(moves.keys())[0]
                second_element_of_moves_dict = list(moves.keys())[1]
                print("\nPlease select your move:\n1. {} (Deal damage between 18-25)\n2. {} (Deal damage between 10-35)\n3. Heal (Restore between 20-25 health)\n".format(first_element_of_moves_dict, second_element_of_moves_dict))

                player_move = input("> ").lower()

                move_miss = random.randint(1, 5)  # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0  # player misses and deals no damage
                    helpers.clear_screen()
                    print("You missed!")
                else:
                    if character_type == "wizard":
                        helpers.clear_screen()
                        if player_move in ("1", "fireball"):
                            player_move = moves["Fireball"]
                            print("\nYou used Fireball. It dealt ", player_move, " damage.")
                        elif player_move in ("2", "spell of destruction"):
                            player_move = moves["Spell of destruction"]
                            print("\nYou used Spell of destruction. It dealt ", player_move, " damage.")
                        elif player_move in ("3", "heal"):
                            heal_up = True  # heal activated
                            player_move = moves["Heal"]
                            print("\nYou used Heal. It healed for ", player_move, " health.")
                        else:
                            print("\nThat is not a valid move. Please try again.")
                            continue
                    
                    if character_type == "warrior":
                        helpers.clear_screen()
                        if player_move in ("1", "sword spike"):
                            player_move = moves["Sword spike"]
                            print("\nYou used Sword spike. It dealt ", player_move, " damage.")
                        elif player_move in ("2", "deadpunch"):
                            player_move = moves["Deadpunch"]
                            print("\nYou used Deadpunch. It dealt ", player_move, " damage.")
                        elif player_move in ("3", "heal"):
                            heal_up = True  # heal activated
                            player_move = moves["Heal"]
                            print("\nYou used Heal. It healed for ", player_move, " health.")
                        else:
                            print("\nThat is not a valid move. Please try again.")
                            continue

                    if character_type == "assassin":
                        helpers.clear_screen()
                        if player_move in ("1", "poisonous dagger spike"):
                            player_move = moves["Poisonous dagger spike"]
                            print("\nYou used Poisonous dagger spike. It dealt ", player_move, " damage.")
                        elif player_move in ("2", "rain of death"):
                            player_move = moves["Rain of death"]
                            print("\nYou used Rain of death. It dealt ", player_move, " damage.")
                        elif player_move in ("3", "heal"):
                            heal_up = True  # heal activated
                            player_move = moves["Heal"]
                            print("\nYou used Heal. It healed for ", player_move, " health.")
                        else:
                            print("\nThat is not a valid move. Please try again.")
                            continue


                # print('-----------------------------------------------------------------------------------------------------')

            else:  # boss turn

                move_miss = random.randint(1, 5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    boss_move = 0  # the boss misses and deals no damage
                    print("The boss missed!")
                else:
                    if boss_health > 30: 
                        if player_health > 75:
                            boss_move = computer_moves["Toxic Bite"]
                            print("\nThe boss used Toxic Bite. It dealt ", boss_move, " damage.")
                        elif player_health > 35 and player_health <= 75:  # boss decides whether to go big or play it safe
                            list_of_moves = ["Toxic Bite", "Furious ultra mega rage attakck"]
                            list_of_moves = random.choice(list_of_moves)
                            boss_move = computer_moves[list_of_moves]
                            print("\nThe boss used ", list_of_moves, ". It dealt ", boss_move, " damage.")
                        elif player_health <= 35:
                            boss_move = computer_moves["Furious ultra mega rage attakck"]  # FINISH HIM!
                            print("\nThe boss used Furious ultra mega rage attakck. It dealt ", boss_move, " damage.")
                    else:  # if the boss has less than 30 health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1, 2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            boss_move = computer_moves["Heal"]
                            print("\nThe boss used Heal. It healed for ", boss_move, " health.")
                        else:
                            if player_health > 75:
                                boss_move = computer_moves["Toxic Bite"]
                                print("\nThe boss used Toxic Bite. It dealt ", boss_move, " damage.")
                            elif player_health > 35 and player_health <= 75:
                                list_of_moves = ["Toxic Bite", "Furious ultra mega rage attakck"]
                                list_of_moves = random.choice(list_of_moves)
                                boss_move = computer_moves[list_of_moves]
                                print("\nThe boss used ", list_of_moves, ". It dealt ", boss_move, " damage.")
                            elif player_health <= 35:
                                boss_move = computer_moves["Furious ultra mega rage attakck"]  # FINISH HIM!
                                print("\nThe boss used Furious ultra mega rage attakck. It dealt ", boss_move, " damage.")

            # print('-----------------------------------------------------------------------------------------------------')

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100  # cap max health at 100. No over healing!
                else:
                    boss_health += boss_move
                    if boss_health > 100:
                        boss_health = 100
            else:
                if player_turn:
                    boss_health -= player_move
                    if boss_health < 0:
                        boss_health = 0  # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player_health -= boss_move
                    if player_health < 0:
                        player_health = 0
                        winner = "boss"
                        break

            print("\nPlayer health: ", player_health, "boss health: ", boss_health)

            # switch turns
            player_turn = not player_turn
            boss_turn = not boss_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nPlayer health: ", player_health, "boss health: ", boss_health)
            print("\nCongratulations! You have won. You're an animal!!")
        else:
            print("\nPlayer health: ", player_health, "boss health: ", boss_health)
            print("\nSorry, but your opponent wiped the floor with you. Better luck next time.")
            health_of_player_in_the_whole_game = 0
        # print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer == "n":
            break
        # if answer not in ("yes", "y"):
            # play_again = False
            break
        break

    # return health_of_player_in_the_whole_game 

# fighting_boss("wizard")

# print(fighting_boss("wizard", 1))

# def win_or_lose(health_of_player_in_the_whole_game)


health_of_player_in_the_whole_game = 0
fighting_boss("wizard", health_of_player_in_the_whole_game)
