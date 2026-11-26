from abc import ABC ,abstractmethod
from domain.inventory import inventory

class Character(ABC):
    def __init__(self,name:str,health:int,attack_power:int):
        self.name = name
        self._health = health #protected
        self.attack_power =  attack_power
        self.__max_health = health #encapsulation
        self.inventory = inventory()
      
      
    @property
    def health(self)-> int:
        return self._health
    
    @property
    def is_alive(self)->bool:
        return self._health > 0
        

    def describe(self)->str:
        return f"{self.name} has {self.health} Hp and {self.attack_power}ATK"
    
    def heal_amount(self,amount:int)->None:
            if amount < 0 :
                raise ValueError("heal amount cannt be negative value")
            self._health = min(self.__max_health,self._health+amount)
            

    def attack(self,target:"Character")->None:
        target._health -= self.attack_power
        if not self.is_alive:
            return
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
  

    def take_damage(self,amount:int)->None:
        if amount < 0 :
            raise ValueError("Damage cannot be neagative")
        # reduce = max(0,amount-self.defense)
        self._health = max(0,self._health-amount)
        
        
    @abstractmethod
    def special_ability(self,target:"Character")->None:
         """Every concrete Character MUST define its own special move."""
         raise NotImplementedError


    # Add this inside the Character.__init__ method:
    # self.inventory = Inventory()
    pass

