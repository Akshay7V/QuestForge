from domain.character import Character
from domain.exceptions import InsufficientManaError
class Warrior(Character):
    def __init__(self, name:str):
        super().__init__(name, health=120, attack_power=18)
        
    def special_ability(self,target:Character)->None:
        bonus = int (self.attack_power * 1.5)
        target.take_damage(bonus)
        print(f"{self.name} uses cleave! {bonus} damage to {target.name}")
        
        
        
class Mage(Character):
        def __init__(self, name:str):
            super().__init__(name, health=80, attack_power=10)
            self.mana = 50
            
        def special_ability(self,target:"Character")->None:
            cost = 20
            if self.mana <cost :
                raise InsufficientManaError(f"{self.name} needs {cost} mana has {self.mana}")
                
            self.mana -= cost
            damage = self.attack_power * 3
            target.take_damage(damage)
            print(f"{self.name} casts fireball!{damage} damage to {target.name}")


class Rouge(Character):
        def __init__(self, name:str):
            super().__init__(name, health=90, attack_power=14)
                
        def special_ability(self,target:Character)->None:
            crit = self.attack_power * 2
            target.take_damage(crit)
            print(f"{self.name}lands a backstab{crit} critical damageto {target.name}")
            
            
class Cleric(Character):
    def __init__(self, name:str):
         super().__init__(name, health=80, attack_power=12)
         
    def special_ability(self,target:Character)->None: 
        target._health += self.health        
        print(f"{self.name} healed {target.name}!{target.name} Hp is {target.health}")
            
            
                
                