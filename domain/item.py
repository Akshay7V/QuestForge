from abc import ABC ,abstractmethod

class item(ABC):
    @abstractmethod
    def apply(self,Character)->str:
        """Apply this item's effect to a character; return a description string."""