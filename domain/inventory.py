class inventory:
    
    
    def __init__(self):
        self._item:list = []
        
    def add(slef,item)->None:
        slef._item.append(item)
        
    def use(self,index:int,target)->str:
        item = self._item.pop(index)
        return item.apply(target)
    
    def list_item(self)->list[str]:
        return [type(i).__name__ for i in self.name]
        