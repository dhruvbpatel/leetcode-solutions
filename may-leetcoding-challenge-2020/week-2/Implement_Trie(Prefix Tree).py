class TreeNode:
    def __init__(self,val):
        self.val=val
        self.endHere=False
        self.children={} ## for storing all our child
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rootNode = TreeNode(None)
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parentNode = self.rootNode

        for i,char in enumerate(word):



            if char not in parentNode.children:
                parentNode.children[char]=TreeNode(char) ## if our child is not present then insert

            parentNode=parentNode.children[char] ## updating the parent

            if(i==len(word)-1): ### reached the end
                parentNode.endHere=True




        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.

        """

        parentNode =self.rootNode

        for i in word:
            if i not in parentNode.children:
                return False
            parentNode = parentNode.children[i]
        return parentNode.endHere


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        parentNode = self.rootNode

        for i in prefix:
            if i not in parentNode.children:
                return False
            parentNode = parentNode.children[i]
        return True  ## we reached the end of prefix and is not false

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)