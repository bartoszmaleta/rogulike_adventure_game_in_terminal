 # Turn Based Battle Simulator

# Player and boss take turns to attack each other with different moves
# until one is defeated.

import random


def fighting_boss():
    """Main function that will welcome the player to the game."""

    print("\tWelcome to Battle Sim! This is a turn based combat simulator where")
    print("\tthere can only be one winner.")

    print("\nHow to play.\n\nPlayers take turn to choose a move. Moves can either deal moderate damage")
    print("with a low range, deal high damage but over a wide")
    print("range, or they can heal. (Note: Moves can miss, including Heal!)")

    print("\nEach player starts with 100 health, and the first")
    print("player to reduce their opponent to 0 is the winner.")

    print("\nThat's it! Good luck")

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        boss_health = 100

        # determine whose turn it is
        turn = random.randint(1, 2)  # heads or tails
        if turn == 1:
            player_turn = True
            boss_turn = False
            print("\nPlayer will attack first.")
        else:
            player_turn = False
            boss_turn = True
            print("\nBoss will attack first.")

        print("\PLAYER HEALTH ", player_health)
        print("BOSS HEALTH: ", boss_health)

        # set up the main game loop
        while (player_health != 0 or boss_health != 0):

            heal_up = False  # determine if heal has been used by the player. Resets false each loop.
            miss = False  # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            moves = {"Deadpunch": random.randint(18, 25),
                     "Fireball": random.randint(10, 35),
                     "Heal": random.randint(20, 25)}

            if player_turn:
                print("\nPlease select your move:\n1. Deadpunch (Deal damage between 18-25)\n2. Fireball (Deal damage between 10-35)\n3. Heal (Restore between 20-25 health)\n")

                player_move = input("> ").lower()
                # player_move = ">>> {} <<<".format(input().lower())

                move_miss = random.randint(1, 5)  # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0  # player misses and deals no damage
                    print("You missed!")
                else:
                    if player_move in ("1", "deadpunch"):
                        player_move = moves["Deadpunch"]
                        print("\nYou used Deadpunch. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "fireball"):
                        player_move = moves["Fireball"]
                        print("\nYou used Fireball. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "heal"):
                        heal_up = True  # heal activated
                        player_move = moves["Heal"]
                        print("\nYou used Heal. It healed for ", player_move, " health.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

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
                            boss_move = moves["Deadpunch"]
                            print("\nThe boss used Deadpunch. It dealt ", boss_move, " damage.")
                        elif player_health > 35 and player_health <= 75:  # boss decides whether to go big or play it safe
                            list_of_moves = ["Deadpunch", "Fireball"]
                            list_of_moves = random.choice(list_of_moves)
                            boss_move = moves[list_of_moves]
                            print("\nThe boss used ", list_of_moves, ". It dealt ", boss_move, " damage.")
                        elif player_health <= 35:
                            boss_move = moves["Fireball"]  # FINISH HIM!
                            print("\nThe boss used Fireball. It dealt ", boss_move, " damage.")
                    else:  # if the boss has less than 30 health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1, 2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            boss_move = moves["Heal"]
                            print("\nThe boss used Heal. It healed for ", boss_move, " health.")
                        else:
                            if player_health > 75:
                                boss_move = moves["Deadpunch"]
                                print("\nThe boss used Deadpunch. It dealt ", boss_move, " damage.")
                            elif player_health > 35 and player_health <= 75:
                                list_of_moves = ["Deadpunch", "Fireball"]
                                list_of_moves = random.choice(list_of_moves)
                                boss_move = moves[list_of_moves]
                                print("\nThe boss used ", list_of_moves, ". It dealt ", boss_move, " damage.")
                            elif player_health <= 35:
                                boss_move = moves["Fireball"]  # FINISH HIM!
                                print("\nThe boss used Fireball. It dealt ", boss_move, " damage.")

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

        print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer == "n":
            break
        # if answer not in ("yes", "y"):
            # play_again = False


fighting_boss()