import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        
        """
        self.d ={}
        self.ind = []
        self.tail=-1
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        
        """
        if val not in self.d:
            
            self.ind.append(val)
            self.tail+=1
            self.d[val]=self.tail  ## dict having key = val and value = tail i.e len(ind) 
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
         
        ## the logic is to pop the last element of array whihc is o(1)
        ### for that we would copy last element to the val element's index in ind
        ### then update the index of last element in dict
        ## pop and del that from dict 
        ## decrease tail
        
        if val in self.d:
            tail_element = self.ind[-1]  ## get last element
            
            self.ind[self.d[val]]=tail_element  ## update the val's index element with last element
            self.d[tail_element]=self.d[val] ## also update index of last element to val's index
            self.ind.pop() ## pop element
            del self.d[val] ## del val
            self.tail-=1 ## decrease tail
            return True
        else:
            return False
        

#         if val in self.d:
#             del self.d[val]
#             self.ind.remove(val)
#             return True
#         else:
#             return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        
        """
        
        return random.choice(self.ind)
        
        
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()