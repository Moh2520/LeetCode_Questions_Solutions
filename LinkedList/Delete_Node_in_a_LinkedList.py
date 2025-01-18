# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        U:  -we have a singlely linkedlist
            - we need to delete a specified node
            - given -> node to be delted
            - not given -> first node of head
            - all values are unique
            - given node is not last node
            - The value of the given node should not exist in the linked list.
            - The number of nodes in the linked list should decrease by one.
            -All the values before node should be in the same order.
            -All the values after node should be in the same order.
        M:
            -linked list 
            - two pointer 
        P:
        
        I:
        R:
        E:
        """
if __name__ == "__main__":
    solution = Solution()

    head = [4,5,1,9]
    node = 5