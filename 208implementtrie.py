class Trie:

    def __init__(self):
        # Pointer to its all 26 childrens
        self.children = [None] * 26
        # Pointer marking end of string
        self.end_of_string = False

        # Eg: "apple" and "apply"
        # "appl" it will be same map, just after it children e and y will be set.
        # its end of string will also be set.
        # Now if we insert "applying" then in y we will set its childrens.
        # only make end of string as true if its the last of the string.
        return
        
    def get_idx(self, char) -> int:
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        # Creating a pointer from the self pointer
        root = self

        for idx in range(len(word)):
            each_char = word[idx]

            # In each character of the pointer now we check if its present.
            # It will be present only if its children is not None.
            # If not present then set it, and then we will have it inserted properly.
            # Then we move forward by making the root as the children of its parent.
            if root.children[self.get_idx(each_char)] is None:
                root.children[self.get_idx(each_char)] = Trie()
            
            # Moving the root forward to its internal children so that insertion happens recursively.
            root = root.children[self.get_idx(each_char)]
        
        root.end_of_string = True


    def search(self, word: str) -> bool:
        root = self
        for each_char in word:
            if root.children[self.get_idx(each_char)] is None:
                return False
            
            root = root.children[self.get_idx(each_char)]
        
        # The traversal is same as Insertion just we need to check if end of string is set.
        # If end of string is set then it means search was successful since we only set it if its end of word.
        # If unset then it means that its only a half word.
        # Eg: search for "apple" in "apples" is going to be returning False as apples will be end of string and not apple.
        return root.end_of_string


    def startsWith(self, prefix: str) -> bool:
        root = self

        for each_char in prefix:
            if root.children[self.get_idx(each_char)] is None:
                return False
            
            root = root.children[self.get_idx(each_char)]
        
        # The traversal is same as search, just we don't need to make sure if its end of string.
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
