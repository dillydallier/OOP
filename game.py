import sys

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
    """defines the game"""

    def setup(self):
        """defines players and monsters"""

        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        """gets a new monster"""

        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        """at each turn, monsters can attack, dodge, or do nothing
        If monsters attack, player may get hit.
        If monsters dodge, player's attack may be unsuccessful.
        If monsters do nothing, player can choose to attack.
        """
        # check to see if the monster attacks
        if self.monster.attack():
            # if so, tell the player
            print("{} is attacking!".format(self.monster))
            # check if the player wants to dodge_limit
            if input("Dodge? Y/n ").lower() == "y":
                # if so, see if the dodge is successful
                if self.player.dodge():
                    # if it is, move on
                    print("You dodged an attack!")
                # if it's not, move one player hit point
                else:
                    print("You got hit anyway!")
                    self.player.hit_points -= 1
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.hit_points -= 1
        # if the monster isn't attacking, tell that to the player
        else:
            print("{} isn't attacking this turn.".format(self.monster))

    def player_turn(self):
        """lets the player attack, rest, or quit"""
        player_move = input("[A]ttack, [R]est or [Q]uit? ").lower()
        # if they attack
        if player_move == "a":
            # see if the attack is successful
            print("You are attacking {}".format(self.monster))
            if self.player.attack():
                # if so, see if the monster dodges
                if self.monster.dodge():
                    # if dodged, print that
                    print("{} dodged your attack!".format(self.monster))
                # if not dodged,
                # subtract the right num of hit points from the monster
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1

                    print(
                        "You hit {} with your {}!"
                        .format(self.monster, self.player.weapon))
            # if not a good attack, tell the player
            else:
                print("You missed!")
        # if they rest:
        elif player_move == "r":
            # call the player.rest() method
            print("You rest and gain 1 hit point.")
            self.player.rest()
        # if they quit, exit the game
        elif player_move == "q":
            sys.exit()
        # if they pick anything else, return this method
        else:
            self.player_turn()

    def cleanup(self):
        """lets player gain experience when the monster dies
        gets a new monster
        """
        # if the monster has no more hit points
        if self.monster.hit_points <= 0:
            # up the player's experience
            self.player.experience += self.monster.experience
            # print a message
            print("You killed {}".format(self.monster))
            # get a new monster
            self.monster = self.get_next_monster()

    def __init__(self):
        """lets player play the game
        prints out win/lose messages at the end of each run
        """
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print("\n" + "="*20)
            print('You: {}'.format(self.player))
            print('The Monster: {}'.format(self.monster))
            self.monster_turn()
            print("-"*20)
            self.player_turn()
            self.cleanup()
            print("\n" + "+"*20)

        if self.player.hit_points:
            print("You win!")
        elif self.monster or self.monsters:
            print("You lose!")
        sys.exit()


Game()
