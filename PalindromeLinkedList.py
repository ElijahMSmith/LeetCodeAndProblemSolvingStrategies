# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindromeNewSpace(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        str = ""
        while head != None:
            str += str(head.val)
            head = head.next

        # Slice notation [startIndex:stopIndex:step]
        return str == str[::-1]

    def isPalindromeConstantSpace(self, head):
        leading, lagging = head, head

        if leading == None or lagging == None:
            return True

        # Move leading twice for every move of lagging once
        while leading.next != None and leading.next.next != None:
            leading = leading.next.next
            lagging = lagging.next

        # If list is even length, leading must move
        # once more to be at the very tail
        if leading.next != None:
            leading = leading.next

        # Reverse all nodes in the second half of the list
        # Point lagging node at the previous node, then move to next
        prev = None
        while lagging != None:
            temp = lagging.next
            lagging.next = prev
            prev = lagging
            lagging = temp

        # Converge from head and tail and check for palindrome
        while head != leading and leading != None and head != None:
            if head.val != leading.val:
                return False
            head = head.next
            leading = leading.next

        return True
