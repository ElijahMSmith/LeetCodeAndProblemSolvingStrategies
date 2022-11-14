
'''
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Utilized an "improvised" implementation of a data structure I came up with a while back
Insertion is done iteratively, and searching is done recursively with search pruning via backtracking
'''

## Uncommented solution in Python3

class WordDictionary:

    def __init__(self):
        self.root = [ {  }, False ];

    def addWord(self, word: str) -> None:

        currentNode = self.root;

        for letter in word:
            childrenMap, isWord = currentNode;
            
            if letter not in childrenMap:
                childrenMap[letter] = [ {  }, False ];
            
            currentNode = childrenMap[letter];
        
        currentNode[1] = True;

    def search(self, word: str) -> bool:
        return self.recSearch(self.root, word, 0);
    
    
    def recSearch(self, currentNode, word, index):
        
        childrenMap, isWord = currentNode;

        if index == len(word):
            return isWord;

        letter = word[index];
        
        if letter != '.':
            if letter in childrenMap:
                return self.recSearch(childrenMap[letter], word, index + 1);

        else:
            for childrenLetter, childrenNode in childrenMap.items():
                if self.recSearch(childrenNode, word, index + 1):
                    return True;
        
        return False;



## Commented solution in Python3

class WordDictionary:

    def __init__(self):
        ## initialize the trie's root node
        self.root = [ {  }, False ];

    def addWord(self, word: str) -> None:
        
        ## start at the root node for insertion
        currentNode = self.root;
        
        ## iterate over letters in the word
        for letter in word:
            childrenMap, isWord = currentNode;
            
            ## if we don't have current letter to continue the word's remaining suffix, create the node
            if letter not in childrenMap:
                childrenMap[letter] = [ {  }, False ];
            
            ## move down there
            currentNode = childrenMap[letter];
        
        ## at this point, you are at the word's terminal letter node. mark as word
        currentNode[1] = True;

    def search(self, word: str) -> bool:
        ## call the recursive solution
        return self.recSearch(self.root, word, 0);
    
    
    def recSearch(self, currentNode, word, index):
        
        childrenMap, isWord = currentNode;

        ## base case -- we are at the maximal length of the search term
        if index == len(word):
            ## return the state of the word's node
            return isWord;
        
        ## get the current letter
        letter = word[index];
        
        ## if we are targeting a specific letter at the current point of the search
        if letter != '.':
            ## if we have that letter as a child of the current prefix, explore
            if letter in childrenMap:
                return self.recSearch(childrenMap[letter], word, index + 1);
        
        ## if we can go down any letter path
        else:
            ## iterate over all possible suffix extension paths from current prefix
            for childrenLetter, childrenNode in childrenMap.items():
                ## recurse, and if we find a solution, prune the search tree early
                if self.recSearch(childrenNode, word, index + 1):
                    return True;
        
        ## otherwise, we have not found anything
        return False;