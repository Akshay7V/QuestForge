
class Character:
    def __init__(self,name:str,health:int,attack_power:int):
        self.name = name
        self.health = health
        self.attack_power =  attack_power
      
        

    def describe(self)->str:
        return f"{self.name} has {self.health} Hp and {self.attack_power}ATK"

    def attack(self,target:"Character")->None:
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        
        
    def heal_amount(self,amount:int)->None:
        self.health += amount
        print(f"{self.name} attack_power is increased by {amount} and now it is {self.health}")


    """Placeholder — fleshed out in Level 1."""
    pass

