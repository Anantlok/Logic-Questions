# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current=head
        res=[]
        while current:
            res.append(current.val)
            current=current.next
        rev = res[::-1]
        if res==rev:
            return True
        else:
            return False
        