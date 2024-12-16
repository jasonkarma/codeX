#simple RPG game with players and enemies\
import random
import pdb

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

#method to attack(target)
    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")
        else:
            print(f"{target.name} has {target.health} health remaining.")

#method to heal(self)
    def heal(self):
        heal_amount = random.randint(1, self.attack_power)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health!")
        print(f"{self.name} has {self.health} health remaining.")

#player class
class Player(Character):
    def __init__(self, name, health, attack_power, level=1, experience=0, gold=0):
        super().__init__(name, health, attack_power)
        self.level = level
        self.experience = experience
        self.gold = gold
        self.inventory = []

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gains {amount} experience points!")
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.attack_power += 2
        self.health += 10
        self.experience -= self.level * 100
        print(f"{self.name} has leveled up to level {self.level}!")

#Enemy Class
class Enemy(Character):
    def __init__(self, name, health, attack_power, enemy_type):
        super().__init__(name, health, attack_power)
        self.enemy_type = enemy_type

# Main Game Loop
def main():
    player = Player("Hero", 100, 10)
    enemies = [
        Enemy("Dragon", 50, 5, "Dragon"),
        Enemy("Goblin", 25, 3, "Goblin")
    ]
    #game loop
    while player.health > 0 and enemies:
        print("\n--- New Turn ---")
        print
        print(f"{player.name}: {player.health} HP, Level {player.level}, Attack Power {player.attack_power}")
        for i, enemy in enumerate(enemies):
            print(f"{i+1}. {enemy.name}: {enemy.health} HP")
        print("\nWhat will you do?")
        print("1. Attack an enemy")
        print("2. Heal")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            index = int(input("Enter the number of the enemy to attack: ")) - 1
            player.attack(enemies[index])
            if enemies[index].health <= 0:
                enemies.pop(index)
                player.gain_experience(50)
        elif choice == "2":
            player.heal()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

        for enemy in enemies:
            if enemy.health > 0:
                enemy.attack(player)



    if player.health <= 0:
        print(f"{player.name} has been defeated!")
    else:
        print(f"Congratulations! You have defeated all enemies and saved the {player.name}!")
        
if __name__ == "__main__":
    main()


