from domain.exceptions import InventoryEmptyError

class inventory:
    
    
    def __init__(self):
        self._item:list = []
        
    def add(slef,item)->None:
        slef._item.append(item)
        
    def use(self,index:int,target)->str:
        if not self._item:
            raise InventoryEmptyError("inventory is empty")
        if index < 0 or index >= len(self._item):
            raise IndexError("invalid item slot")
        item = self._item.pop(index)
        return item.apply(target)
       
        
    
    def list_item(self)->list[str]:
        return [type(i).__name__ for i in self.name]
        