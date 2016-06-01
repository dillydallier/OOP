from combat import Combat
import random


COLORS = ["yellow", "red", "blue", "green", "pink", "black", "purple", "grey"]


class Monster(Combat):
    """gives initial setup for monsters"""
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = "sword"
    sound = "roar"

    def __init__(self, **kwargs):
        """generates random stats for monsters"""
        self.hit_points = random.randint(
                                        self.min_hit_points,
                                        self.max_hit_points)
        self.experience = random.randint(
                                        self.min_experience,
                                        self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """prints message at each turn"""
        return "{} {}, HP: {}, XP: {}".format(
                                            self.color.title(),
                                            self.__class__.__name__,
                                            self.hit_points,
                                            self.experience)

    def battlecry(self):
        """lets monster cries out loud in battle"""
        return self.sound.upper()


class Goblin(Monster):
    """defines Goblin the mosnter"""
    max_hit_points = 3
    max_experience = 2
    sound = "squeak"


class Troll(Monster):
    """defines Troll the monster"""
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = "growl"


class Dragon(Monster):
    """defines Dragon the monster"""
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = "raaaaaaaaaar"
