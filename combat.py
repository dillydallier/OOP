import random


class Combat:
    """gives options for each turn"""
    dodge_limit = 6
    attack_limit = 6

    def dodge(self):
        """lets player/monster dodge"""
        roll = random.randint(1, self.dodge_limit)
        return roll > 4

    def attack(self):
        """lets player/monster attack"""
        roll = random.randint(1, self.attack_limit)
        return roll > 4
