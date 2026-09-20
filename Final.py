import random


class character:
    def __init__(self, health, defense, strength, name):
        self.health = health
        self.name = name
        self.defense = defense
        self.strength = strength

    def getName(self):
        print(self.name)

    def take_damage(self, damage):
        damage_taken = damage - self.defense
        self.health -= damage_taken
        return damage_taken

    def attack(self, target):
        damage = self.strength * 2
        damage_dealt = target.take_damage(damage)
        return damage_dealt

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
        return self.health < 0
        if self.health < 0:
            print("Game Over!")


Rare = False
Medium = False
Burnt = False

class Sorcerer(character):
    def attack(self, target):
        dexterity = 30
        critical_hit = random.randint(5, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


class Warlock(character):
    def attack(self, target):
        dexterity = 15
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt

class Mage(character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt

class Monk(character):
    def attack(self, target):
        dexterity = 32
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


class Wizard(character):
    def attack(self, target):
        dexterity = 35
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


class Bard(character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


class Rogue(character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


class Fighter(character):
    def attack(self, target):
        dexterity = 25
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


class Dragon(character):
    def attack(self, target):
        dexterity = 25
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


class IceGiant(character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


class MimicChest(character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt

class Warrior(character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt

class Admin(character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) < dexterity
        damage = self.strength * 4
        if critical_hit:
            damage *= 4
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt



name = input("Enter your name:")
answerChosen = False
while not answerChosen:
    answer = input("Choose your Class: Fighter, Rogue, Bard, Wizard, Monk, Warlock, Sorcerer, Mage, Warrior:")

    difficulty = input("Choose your difficulty: Rare, Medium, or Burnt:")
    if difficulty == "Rare":
        Rare = True
    elif difficulty == "Medium":
        Medium = True
    else:
        Burnt = True

    if answer == "Fighter":
        print("Fighter class chosen! Be ready for battle.")
        p1 = Fighter(60, 8, 20, name)
        answerChosen = True
    if answer == "Rogue":
        print("Rogue class chosen! Be ready for battle.")
        p1 = Rogue(80, 9, 20, name)
        answerChosen = True
    if answer == "Bard":
        print("Bard class chosen! Be ready for battle.")
        p1 = Bard(88, 10, 20, name)
        answerChosen = True
    if answer == "Wizard":
        print("Wizard class chosen! Be ready for battle.")
        p1 = Wizard(66, 8, 17, name)
        answerChosen = True
    if answer == "Monk":
        print("Monk class chosen! Be ready for battle.")
        p1 = Monk(54, 10, 30, name)
        answerChosen = True
    if answer == "Warlock":
        print("Warlock class chosen! Be ready for battle")
        p1 = Warlock(80, 14, 25, name)
        answerChosen = True
    if answer == "Sorcerer":
        print("Sourcerer class chosen! Be ready for battle")
        p1 = Sorcerer(75, 17, 20, name)
        answerChosen = True
    if answer == "Mage":
        print("Mage class chosen! Be ready for battle")
        p1 = Mage(70, 17, 25, name)
        answerChosen = True
    if answer == "Admin":
        print("Testing phase begin!")
        p1 = Admin(100, 120, 100, name)
        answerChosen = True
    if answer == "Warrior":
        print("Warrior class chosen! Be ready for battle.")
        p1 = Fighter(50, 8, 50, name)
        answerChosen = True

    else:
        print("Restart and pick again.")


def simBattle(p1, p2):
    print(p1.name + " vs. " + p2.name)
    print(str(p1.health) + " vs. " + str(p2.health))

    while p1.is_alive() and p2.is_alive():
        print(p1.name + ": " + str(p1.health))
        print(p2.name + ": " + str(p2.health))
        if p1.is_alive():
            damage = p1.attack(p2)
            print(p1.name + " Attacks " + p2.name + " for " + str(damage))
        if p2.is_alive():
            damage = p2.attack(p1)
            print(p2.name + " Attacks " + p1.name + " for " + str(damage))
        if p1.is_alive()and not p2.is_alive():
            print(p1.name + " Victory!")
            return True
        elif p2.is_alive()and not p1.is_alive():
            print(p2.name + " Victory!")
            return False


if Rare:
    p2 = Dragon(80, 20, 20, "Gertrude")
    p4 = IceGiant(50, 50, 10, "Cryo")
    p5 = MimicChest(30, 30, 50, "Chompers")

if Medium:
    p2 = Dragon(80, 20, 25, "Gertrude")
    p4 = IceGiant(50, 50, 15, "Cryo")
    p5 = MimicChest(40, 30, 45, "Chompers")

if Burnt:
    p2 = Dragon(80, 20, 30, "Gertrude")
    p4 = IceGiant(50, 50, 20, "Cryo")
    p5 = MimicChest(40, 35, 50, "Chompers")

enemyList = [p2, p4, p5]
winner = simBattle(p1, p2)
i = 1
j = 2
while  i in range(3):
    winner == True
    p2 = enemyList[i]
    winner = simBattle(p1, p2)
    i += 1


def simTourney(p1, enemyList):
    p2 = enemyList[0]

    winner = simBattle(p1, p2)
    i = 1
    j = 2
    while (winner == True):
        p2 = enemyList[i]
        winner = simBattle(p1, p2)
        i += 1
    while (winner == True):
        p4 = enemyList[j]
        winner = simBattle(p1, p2)
        i += 1


