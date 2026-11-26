from domain.item import item

class HealthPotion(item):
    def __init__(self,heal_amount:int= 25):
        self.heal_amount = heal_amount
        
        
    def apply(self,character)->str:
        character.heal(self.heal_amount)
        return f"{character.name} drinks a potion and heal{self.heal_amount} HP"
    
class weapon(item):
    def __init__(self,name:str,bonus_attack:int):
        self.name = name
        self.bonus_attack = bonus_attack
        
    def apply(self,character)->str:
        character.attack_power += self.bonus_attack
        return f"{character.name} equips {self.name} (+{self.bonus_attack}ATK)"
    
    
# class Armor(item):
#     def __init__(self,name:str,defense:int):
#         if defense > 0:
#            raise ValueError("defense cannot negative")
#         self.name = name
#         self.defense = defense
        
        
#         @property
#         def defense(self)->str:
#             return self._defense + (self.Armor.defense if self.Armor else 0)
        
#         def equip_armor(self,armor:Armor)->None:
#             self.armor = armor
            
       
       
       