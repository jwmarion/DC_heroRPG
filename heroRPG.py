"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class character(object):
    def __init__(self, health, power):
        pass
    def print_status(self):
        print "You have %d health and %d power." % (self.health, self.power)

    def attack(self, character):
        character.health -= self.power
        print "%s does %d damage to the %s." % (self.type, self.power, character.type)
        if self.type != "Zombie":
            if character.health <= 0:
                print "The %s is dead" % character.type
        else:
            print "ZOMBIE IS IMMORTAL"
            self.health += 100
            if character.health <= 0:
                print "The %s is dead" % character.type

class hero(character):
    def __init__(self,health,power):
        self.health = health
        self.power = power
        self.type = "Hero"

class goblin(character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.type = "Goblin"

class zombie(character):
    def __init__(self,health,power):
        self.health = health
        self.power = power
        self.type = "Zombie"

def main():
    h = hero(10,5)
    g = goblin(6,2)
    z = zombie(6,1)


    while z.health > 0 and h.health > 0:


        print
        print "What do you want to do?"
        print "1. fight monster"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            h.attack(z)

        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if z.health > 0:
            z.attack(h)

main()
