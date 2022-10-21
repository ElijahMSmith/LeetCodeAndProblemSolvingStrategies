'''

230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

The approach uses the inorder traversal of a binary tree (important as this is a BST) and leverages pass by reference to avoid global variables.
'''

## Uncommented solution in Python3

class Solution:
    
    def go(self, root, k):
        if root == None:
            return root;
        
        left = self.go(root.left, k);
        
        if left != None:
            return left;
        
        k[0] -= 1;
        
        if k[0] == 0:
            return root;
        
        return self.go(root.right, k);
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ans = self.go(root, [k]);

        return ans.val;


## Commented solution in Python3

class Solution:
    
    def go(self, root, k):

        ## If we cannot progress, stop and return None
        if root == None:
            return root;
        
        ## This will store the result from the left subtree of the current node
        left = self.go(root.left, k);
        
        ## If we have a non-None result, we have found the Kth-Smallest in the BST on the left of the current node
        if left != None:
            return left;
        
        ## Otherwise, we have not. Since k is 1-indexed, decrement first then check if we have a match
        k[0] -= 1;
        
        ## If the counter that started at k is now at 0, this is the Kth-Smallest in the BST, return the current node
        if k[0] == 0:
            return root;
        
        ## Otherwise, try to find it to the right of the current node and account for the nodes in the right subtree of the current node
        return self.go(root.right, k);
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ## This stores the answer node
        ans = self.go(root, [k]);

        ## Return the value at that answer node
        return ans.val;
