from domain.character import Character


if __name__ == "__main__":
    hero = Character("Aria",100,15)
      
    goblin = Character("Goblin",50,5)
    

    print(hero.describe())
    print(goblin.describe())
    

    hero.attack(goblin)
    hero.take_damage(10)
    print(f"hero got damage and balance health {hero.health} ")
    print(goblin.describe())
    
   

    