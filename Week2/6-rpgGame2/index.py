#!/usr/bin/env python3

"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import random
import time

class Character(object):
    def __init__(self, name, health, power, coins, frozen=False):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.frozen = frozen

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        if self.power == 0:
            print('{} unable to attack {}'.format(self.name, enemy.name))
        else:
            print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power, self)
        time.sleep(1.5)

    def receive_damage(self, points, enemy):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        # If Hero dies before Enemy
        if self == hero:
            if not self.alive():
                return
        # If Enemy dies before Hero
        if not self.alive():
            enemy.coins += self.coins
            print("{} is dead.".format(self.name))
            print("{} received {} coins in loot.".format(enemy.name, self.coins))
            print("{} total coins".format(enemy.coins))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        super().__init__('hero', 10, 2, 20)

    def attack(self, enemy):
        attackBonus = random.random() <= 0.2
        if attackBonus:
            self.power = self.power * 2
            return super(Hero, self).attack(enemy)
        return super(Hero, self).attack(enemy)

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        super().__init__('goblin', 6, 2, 5)

class Wizard(Character):
    def __init__(self):
        super().__init__('wizard', 8, 1, 6)

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        super().__init__('medic', 8, 1, 6)

    def receive_damage(self, points, enemy):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))
        regenHealth = random.random() <= 0.2
        if regenHealth <= 20:
            self.health += 2
            print('{} gained 2 health'.format(self.name))

class Shadow(Character):
    def __init__(self):
        super().__init__('shadow', 1, 2, 7)
        self.hits = 0

    def receive_damage(self, points, enemy):
        self.hits += 1
        if self.hits == 10:
            self.hits = 0
            self.health -= points
            super(Shadow, self).receive_damage(points)
        else:
            print("{} received 0 damage.".format(self.name))
        
class Zombie(Character):
    def __init__(self):
        super().__init__('zombie', 5, 2, 9)

    def receive_damage(self, points, enemy):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            self.health = 5
            print('{} regains health'.format(self.name))

class Saiyan(Character):
    def __init__(self):
        super().__init__('saiyan', 13, 2, 15)
        self.activateCharge = False
        self.charge = 3

    def attack(self, enemy):
        if self.activateCharge:
            self.charge -= 1
            if self.charge == 0:
                self.charge = 3
                if self.frozen:
                    super(Saiyan, self).attack(enemy)
                else:
                    print('Charge complete!')
                    print('{} unleashes powerful attack!'.format(self.name))
                    super(Saiyan, self).attack(enemy)
            else:
                print('{} is charging attack'.format(self.name))
                self.power = 0
                super(Saiyan, self).attack(enemy)
        else:
            self.activateCharge = random.random() <= 0.2
            if self.activateCharge:
                print('{} is charging attack'.format(self.name))
                self.power = 0
                super(Saiyan, self).attack(enemy)
            else:
                self.power = 2
                super(Saiyan, self).attack(enemy)

class Subzero(Character):
    def __init__(self):
        super().__init__('subzero', 11, 2, 13)
        self.frozen = False
        self.frozenCount = 2
        self.enemyPower = 0

    def attack(self, enemy):
        if self.frozen:
            if self.frozenCount == 0:
                self.frozenCount = 2
                enemy.power = self.enemyPower
                self.enemyPower = 0
                print('ENEMY POWER WHEN UNFROZEN', enemy.power)
                print('{} is unfrozen'.format(enemy.name))
                super(Subzero, self).attack(enemy)
            else:
                self.frozenCount -= 1
                self.enemyPower = enemy.power
                enemy.power = 0
                print('{} is frozen'.format(enemy.name))
                super(Subzero, self).attack(enemy)
        else:
            self.frozen = random.random() <= 0.3
            if self.frozen:
                self.frozenCount -= 1
                enemy.power = 0
                print('{} is frozen'.format(enemy.name))
                super(Subzero, self).attack(enemy)
            else:
                super(Subzero, self).attack(enemy)


class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the {}".format(enemy.name))
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            keyinput = int(input())
            if keyinput == 1:
                hero.attack(enemy)
            elif keyinput == 2:
                pass
            elif keyinput == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input {}".format(input))
                continue
            enemy.attack(hero)
        if hero.alive():
            print("You defeated the {}".format(enemy.name))
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            input = int(input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

if __name__ == "__main__":
    hero = Subzero()
    enemy = Goblin()
    enemies = [Subzero(), Subzero()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
    # shopping_engine.do_shopping(hero)

    print("YOU WIN!")