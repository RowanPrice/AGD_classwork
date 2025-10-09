import random

def dice_sum(num_dice:int = 1,num_sides:int = 6):
    """returns the sum of num_dice dice, each with num_sides sides"""
    return sum(random.randint(1, num_sides) for _ in range(num_dice))
print(dice_sum(2,6))

class Character:

    def __init__(self, name:str , skill:int , stamina:int , roll , score):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self):
        return f"Character('{self.name}',{self.skill},{self.stamina})"

    def find_score(self):
        self.roll = dice_sum(2,6)
        self.score = self.skill + self.roll