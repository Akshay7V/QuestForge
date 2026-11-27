from domain.character import Character
from domain.classes import Warrior,Mage,Cleric,Rouge
from domain.battle import run_special_round,total_party_damage
from domain.exceptions import QuestForgeError,InventoryEmptyError
from domain.inventory import inventory


if __name__ == "__main__":
    # hero = Character("Aria",100,15)
    
    # goblin = Character("Goblin",50,5)
    

    # print(hero.describe())
    # print(goblin.describe())
    

    # hero.attack(goblin)
    # hero.take_damage(10)
    # print(f"hero got damage and balance health {hero.health} ")
    # hero.heal_amount(5)
    # print(f"hero healed and balance health is {hero.health}")
    # print(goblin.describe())
    
    print("---------------------------------------------------------------------------")
    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    cleric = Cleric("Kade")
    inv = inventory()
    
    try:     
        mage.special_ability(warrior)
        mage.special_ability(warrior)
        mage.special_ability(warrior) 
        
    except QuestForgeError as e:
        print(f"Action failed: {e}")
        
        
    try:
        inv.use(0,warrior)
        inv.use(1,warrior)
    except InventoryEmptyError as f:
        print(f"Action failed {f}")
        
        
    print(f"Bram HP:{warrior.health},sylla HP: {mage.health}")
    print("---------------------------------------------------------------------------")
    print(f"{cleric.name} heals {warrior.name} for {cleric.health} Hp!Now,{warrior.name} have {warrior.health}Hp!")
    print("---------------------------------------------------------------------------")

    if __name__ == "__main__":
        party = [Warrior("Bram"),Mage("Sylla"),Rouge("d.cruse"),Cleric("Kade")]
        dummy = Warrior("training Dummy")
        
        for member in party:
            run_special_round(member,dummy)
            print(f"Dummy HP : {dummy.health}\n")
            print("---------------------------------------------------------------------------")
            
            # for member1 in party:
                
            #     total_party_damage(member1,dummy)  
            #     total_damage += member1.health(dummy)  
            #     print(f"Dummy HP : {dummy.health}\n")               
            
        
            
    # Replace the `for member1 in party:` loop with just this:
            total_party_damage(party, dummy)
            print(f"Dummy HP : {dummy.health}\n")

            

    
    
    
    
    
    
    
   

    