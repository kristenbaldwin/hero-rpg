#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Hero(Character):
    def attack(self, goblin_enemy):
        goblin_enemy.health -= self.power
        #print(goblin_enemy.health)
        print("You do {} damage to the goblin.".format(self.power))
        if goblin_enemy.health <= 0:
            print("The goblin is dead.")

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

        

class Goblin(Character):
    def attack(self, hero): # Goblin attacks hero            
            hero.health -= self.power
            print("The goblin does {} damage to you.".format(self.power))
            if hero.health <= 0:
                print("You are dead.")

    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

def main():
    hero1 = Hero(10,5)
    goblin1 = Goblin(6,2)

    while goblin1.alive() and hero1.alive():
        hero1.print_status()
        goblin1.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero1.attack(goblin1)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin1.health > 0:
            goblin1.attack(hero1)
 

main()
