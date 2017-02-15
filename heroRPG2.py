#heroRPG2

"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.evade = 1
        self.armor = 0
        self.inventory = []

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        if random.randrange(1,5) == 1:
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)
        # time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= (points - self.armor)
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)


class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.evade = 1
        self.armor = 2
        self.inventory = []

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        # time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        self.inventory.append(item)
        # item.apply(hero)

    def useItem(self,item):
        item.apply(hero)

class Medic(Hero):
    def __init__(self):
        self.name = 'medic'
        self.health = 12
        self.power = 3
        self.coins = 25
        self.evade = 2
        self.armor = 1
        self.inventory = []

    def receive_damage(self, points):
        super(Medic, self).receive_damage(points)
        if random.randrange(1,5) == 1:
            self.health += 2
            print "%s healed 2 damage" % (self.name)


class Shadow(Hero):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 5
        self.coins = 10
        self.evade = 7
        self.armor = 0
        self.inventory = []


class Pacifist(Hero):
    def __init__(self):
        self.name = 'pacifist'
        self.health = 20
        self.power = 0
        self.coins = 5
        self.evade = 3
        self.armor = 2
        self.inventory = []

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s tells %s that there is a better way!" % (self.name, enemy.name)
        if random.randrange(1,20) == 1:
            enemy.health = 0
            print "The %s ran away to work on himself." % (enemy.name)
        # time.sleep(1.5)

class James(Hero):
    def __init__(self):
        self.name = 'james'
        self.health = 10
        self.power = 3
        self.coins = 8
        self.evade = 1
        self.armor = 0
        self.inventory = []

        def attack(self, enemy):
            if not self.alive():
                return
            for x in (random.randrange(1,4)):
                print "%s attacks %s" % (self.name, enemy.name)
                if random.randrange(1,5) == 1:
                    enemy.receive_damage(self.power * 2)
                else:
                    enemy.receive_damage(self.power)
            # time.sleep(1.5)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 5
        self.armor = 1


class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power = 2
        self.coins = 10
        self.armor = 10



class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 6
        self.armor = 0

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            # time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "4. use item"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            elif input == 4:
                for x in range(0,len(hero.inventory)):
                    print "(%d) %s" % (x, hero.inventory[x].name)
                    c =int(raw_input("Which item?> "))
                    if (c < len(hero.inventory)):
                        hero.useItem(hero.inventory[c])
                    else:
                        print "nope"

            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            print "You gained %d coins!" % enemy.coins
            hero.coins += enemy.coins
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    type = 'any'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    type = 'any'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class SuperTonic(object):
    cost = 10
    name = "Super Tonic!"
    type = 'any'
    def apply(self, character):
        character.health += 10
        print "%s's health increased to %d" % (character.name, character.health)

class EvadePotion(object):
    cost = 12
    name = "Dodgy potion"
    type = 'any'
    def apply(self, character):
        character.evade += 2
        print "%s's evade stat increased to %d" % (character.name, character.evade)

class ArmorPotion(object):
    cost = 8
    name = "Armor potion"
    type = 'any'
    def apply(self, character):
        character.armor += 2
        print "%s's armor stat increased to %d" % (character.name, character.armor)

class AcidicSlime(object):
    cost = 3
    type = 'battle'
    name = "Acidic Slime!"
    def apply(self, character):
        enemy.armor = 0
        print "%s's armor stat is now %d!" % (enemy.name, enemy.armor)

class SwapPotion(object):
    cost = 3
    type = 'battle'
    name = "Swap Potion"
    def apply(self, character):
        print "%s swaps power with %s during attack" % (character.name, enemy.name)
        character.power, enemy.power = enemy.power, character.power
        character.attack(enemy)
        character.power, enemy.power = enemy.power, character.power





class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, EvadePotion, ArmorPotion, AcidicSlime, SwapPotion]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                if item.cost <= hero.coins:
                    hero.buy(item)
                    t = raw_input("Use item now? (y/n)")
                    if t == 'y' and (item.type != 'battle'):
                        item.apply(hero)
                else:
                    print "Item costs too much!"


enemies = [Goblin(), Wizard(), Zombie(), ]
battle_engine = Battle()
shopping_engine = Store()

print "What class would you like to use?"
print "(1) Hero\n(2) Medic\n(3) Shadow\n(4) Pacifist\n(5) James"
inp = int(raw_input("> "))

if inp == 1:
    hero = Hero()
    print "hero"
elif inp == 2:
    hero = Medic()
    print "Medic"
elif inp == 3:
    hero = Shadow()
    print "Shadow"
elif inp == 4:
    hero = Pacifist()
    print "Pacifist"
elif inp == 5:
    hero = James()
    print "James"
else:
    print "Fail"




for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
