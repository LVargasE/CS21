# -*- coding: utf-8 -*-
"""
Invent with Python OOP example
"""

class LivingThing():
    def __init__(self, name, health, magicPoints, inventory):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints
        self.inventory = inventory
        self.hunger = 0 # all living things start with hunger level 0
        
    def takeDamage(self, dmgAmount):
        self.health = self.health - dmgAmount
        if self.health == 0:
            print(self.name + ' is dead!')

class Dragon(LivingThing):
    def __init__(self, name, health, magicPoints, inventory, breathType):
        LivingThing.__init__(self, name, health, magicPoints, inventory)        
        self.breathType = breathType
    
# Create the LivingThing object for the hero.
hero = LivingThing('Elsa', 50, 80, {})

monsters = []
monsters.append(LivingThing('Goblin', 20, 0, {'gold': 12, 'dagger': 1}))

dragon = Dragon('Agneel', 300, 200, {'gold': 890, 'magic amulet': 1}, 'Fire')

print('The hero %s has %s health.' % (hero.name, hero.health))
hero.takeDamage(10) # Elsa takes 10 points of damage
print('The hero "{} has {}" health.' .format(hero.name, hero.health))
print('The dragon %s has %s health.' % (dragon.name, dragon.health))
