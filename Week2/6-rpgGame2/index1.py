"""RPG Game"""
import random
#################### Heroes & Enemies #####################
class Character():
    """Parent for all Heroes and Enemies"""
    def __init__(self, name, health, power, magicPoints):
        self.name = name
        self.health = health
        self.power = power
        self.magicPoints = magicPoints
        self.negEffects = {}
        self.posEffects = {}
        self.coins = 0
        self.level = 1
        self.exp = 0
        self.backpack = {}
        self.reward = random.randint(2, 12)

    def meleeAttack(self, enemy):
        if not self.alive():
            self.isDead(enemy)
            return
        if self.isNegEffects(enemy):
            return
        if self.isPosEffects(enemy):
            return
        if enemy.evadeAttack():
            return
        self.decreaseEnemyHealth(enemy)

    def decreaseEnemyHealth(self, enemy):
        attackPower = 0
        armor = self.armor * 1
        if self == hero:
            attackPower = round(((self.power * self.strength) * 0.3) + self.power)
        else:
            attackPower = round((((self.power * self.strength) * 0.3) + self.power) + enemy.level)
        if enemy.weakness == self.element:
            print('Critical Hit!')
            attackPower = (attackPower * 2) - armor
        if attackPower <= 0:
            attackPower = 0
        enemy.health = enemy.health - attackPower
        print('{} received {} damage'.format(enemy.name, attackPower))
        self.isDead(enemy)

    def isDead(self, enemy):
        if enemy == hero:
            if not enemy.alive():
                print('YOU DIED!')
                return
        if not enemy.alive():
            print("You defeated the {}".format(enemy.name))
            # Coin drop increases with Hero level
            coins = self.reward * self.level
            self.coins += coins
            print("{} received {} coins in loot.".format(self.name, coins))
            print("{} total coins".format(self.coins))
            self.gainExp()
            print('{} exp until Level Up'.format(5 - self.exp))
            self.isLevelUp()

    def isLevelUp(self):
        if self.exp % 5 == 0:
            self.exp = 0
            print('{} Leveled Up!'.format(self.name))
            self.level += 1
            self.allocateAttribute()
    
    def allocateAttribute(self):
        allocated = False
        while not allocated:
            print('=====================')
            print('Increase 1 Attribute')
            print('=====================')
            print('1. Evade (Higher chance of avoiding attacks)')
            print('2. Armor (Reduce damage received)')
            print('3. Magic (Increase magic attack damge)')
            print('4. Strength (Increase melee attack damage)')
            response = 0
            try:
                response = int(input('> '))
            except ValueError:
                print('Invalid Command')
                continue
            if response == 1:
                if not self.isAttributeMax(self.evade):
                    self.evade += 1
                    allocated = True
                    print('Evade has increased')
            elif response == 2:
                if not self.isAttributeMax(self.armor):
                    self.armor += 1
                    allocated = True
                    print('Armor has increased')
            elif response == 3:
                if not self.isAttributeMax(self.magic):
                    self.magic += 1
                    allocated = True
                    print('Magic has increased')
            elif response == 4:
                if not self.isAttributeMax(self.strength):
                    self.strength += 1
                    allocated = True
                    print('Strength has increased')
            else:
                print('Invalid Command')
            self.showAttributes()

    def showAttributes(self):
        print('Evade = {}'.format(self.evade))
        print('Armor = {}'.format(self.armor))
        print('Magic = {}'.format(self.magic))
        print('Strength = {}'.format(self.strength))

    def isAttributeMax(self, attribute):
        if attribute == 5:
            print('Attribute is already maxed out'.format())
            return True

    def evadeAttack(self):
        if random.random() < (self.evade * 0.15):
            print('{} evaded attack'.format(self.name))
            return True
        return False

    def printStatus(self):
        print("{} has {} health, {} power, {} magic points, {} element.".format(self.name, self.health, self.power, self.magicPoints, self.element))

    def alive(self):
        return self.health > 0

    def flee(self):
        if random.random() <= 0.3:
            print('{} ran away'.format(self.name))
            return True
        else:
            print('{} could not run away'.format(self.name))
            return False

    def checkMagicPoints(self):
        if self.magicPoints - self.cost >= 0:
            return True
        print('Not enough magic points to use ability')
        return False

    def isNegEffects(self, enemy):
        for key in self.negEffects:
            if key == 'frozen':
                self.negEffects[key] -= 1
                if self.negEffects[key] == 0:
                    del self.negEffects[key]
                    print('{} is unfrozen'.format(self.name))
                else:
                    print('{} is Frozen, unable to attack'.format(self.name))
                return True
        return False

    def isPosEffects(self, enemy):
        for key in self.posEffects:
            if key == 'wolf':
                self.posEffects[key] -= 1
                if self.posEffects[key] == 0:
                    del self.posEffects[key]
                    print('{}\'s Wolf disappears'.format(self.name))
                    break
                else:
                    wolfAttack = round(((self.magic * 6) * 0.5))
                    enemy.health -= wolfAttack
                    print('Wolf attacks {} for {} damage'.format(enemy.name, wolfAttack))
            if key == 'energy':
                self.posEffects[key] -= 1
                if self.posEffects[key] == 0:
                    del self.posEffects[key]
                    energyAttack = round(((self.magic * 40) * 0.4))
                    enemy.health -= energyAttack
                    print('{} completes charge!'.format(self.name))
                    print('{} received {} damage'.format(enemy.name, energyAttack))
                    return True
                else:
                    print('{} is still charging'.format(self.name))
                    return True

    def gainExp(self):
        self.exp += 1
        print('1 EXP gained')

class WhiteWalker(Character):
    """White Walker with Freeze and Ice Burn special ability"""
    def __init__(self):
        super().__init__('White Walker', 20, 3, 10 )
        # Attributes
        self.evade = 2
        self.armor = 1
        self.magic = 1
        self.cost = 5
        self.strength = 1
        self.element = 'ice'
        self.weakness = 'fire'

    def magicAttack(self, enemy):
        """"Ice attack that feezes enemy for 2 turns"""
        if self.checkMagicPoints():
            for key in enemy.negEffects:
                if key == 'frozen':
                    print('Enemy already Frozen')
                    return False
            self.magicPoints -= self.cost
            enemy.negEffects['frozen'] = 3
            print('{} is Frozen for {} turns'.format(enemy.name, enemy.negEffects['frozen'] - 1))
            return True
        return False

class Crusader(Character):
    """Crusader with pet Wolf special ability"""
    def __init__(self):
        super().__init__('Crusader', 18, 4, 14)
        # Attributes
        self.evade = 1
        self.armor = 2
        self.magic = 1
        self.cost = 7
        self.strength = 2
        self.element = 'ground'
        self.weakness = 'ice'

    def magicAttack(self, enemy):
        """"Summons pet wolf that attacks for 2 turns"""
        if self.checkMagicPoints():
            for key in self.posEffects:
                if key == 'wolf':
                    print('Wolf already summoned')
                    return False
            self.magicPoints -= self.cost
            self.posEffects['wolf'] = 3
            print('{} summons Wolf for {} turns'.format(self.name, self.posEffects['wolf'] - 1))
            return True
        return False           

class Saiyan(Character):
    """Saiyan with Power Ball ability"""
    def __init__(self):
        super().__init__('Saiyan', 2300, 200, 10)
        # Attributes
        self.evade = 1
        self.armor = 5
        self.magic = 1 
        self.cost = 10
        self.strength = 1
        self.element = 'fire'
        self.weakness = 'ground'

    def magicAttack(self, enemy):
        """"Powerful Energy Ball that takes 2 turns to charge"""
        if self.checkMagicPoints():
            for key in self.posEffects:
                if key == 'energy':
                    print('Already charging Energy Ball')
                    return False
            self.magicPoints -= self.cost
            self.posEffects['energy'] = 3
            print('{} is charging Energy Ball for {} turns'.format(self.name, self.posEffects['energy'] - 1))
            return True
        return False  

#################### Battle ##################################
class Battle():
    def startBattle(self, hero, enemy):
        print("=====================")
        print("{} faces the {}".format(hero.name, enemy.name))
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.printStatus()
            enemy.printStatus()
            print("-----------------------")
            print("1. Melee Attack")
            print('2. Magic Attack')
            print("3. Pass Turn")
            print("4. Flee")
            print("5. Use Item")
            response = 0
            try:
                response = int(input('> '))
            except ValueError:
                print('Invalid Command')
                continue          
            if response == 1:
                hero.meleeAttack(enemy)
                enemy.meleeAttack(hero)
            if response == 2:
                    if hero.magicAttack(enemy):
                        enemy.meleeAttack(hero)
            elif response == 3:
                enemy.attack(hero)
                pass
            elif response == 4:
                if hero.flee():
                    return 'flee'
                enemy.meleeAttack(hero)
            elif response == 5:
                # Work on at a later date
                pass
        if hero.alive():
            return True
        else:
            return False

######################### Start Game ##################################
if __name__ == "__main__":
    hero = Saiyan()
    battleGround = Battle()
    # shopping = Store()


######################### Main Menu ###############################
while True:
    print("=====================")
    print("      Main Menu      ")
    print("=====================")
    print("1. Battle")
    print('2. Shop')
    print("3. Save")
    print("4. Quit")
    response = 0
    try:
        response = int(input('> '))
    except ValueError:
        print('Invalid Command')
        continue
    if response == 1:
        enemies = [WhiteWalker(), Crusader(), Crusader(), Crusader(), Crusader(), WhiteWalker(), Crusader(), Crusader(), Saiyan(), Crusader(), Saiyan(), Crusader(), Crusader()]
        for enemy in enemies:
            heroWon = battleGround.startBattle(hero, enemy)
            if heroWon == 'flee':
                break
            if not heroWon:
                print("YOU LOSE!")
                exit(0)
    # elif response == 2:

    else:
        print("YOU WIN!")

########################## Store ##################################
# class Store()
#     def shop(self):
#         self.items = [MagicPotion, HealthPotion, EvadePotion, StrengthPotion, ElementChange, FreezePotion]


