from domain.character import Character


if __name__ == "__main__":
    hero = Character("Aria",100,15)
    goblin = Character("Goblin",50,5)
    ogre = Character("Ogre",20,3)

    print(hero.describe())
    print(goblin.describe())
    print(ogre.describe())

    hero.attack(goblin)
    goblin.health -= 15
    print(goblin.describe())
    
    ogre.attack(hero)
    print(hero.describe())
    
    hero.heal_amount(5)
    goblin.heal_amount(5)
    ogre.heal_amount(5)
    
    print(hero.describe())
    print(goblin.describe())
    