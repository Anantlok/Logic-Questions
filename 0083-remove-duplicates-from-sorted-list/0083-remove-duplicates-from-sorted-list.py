# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        lis=[]
        while curr:
            lis.append(curr.val)
            curr=curr.next
        lis=sorted(list(set(lis)))
        dummy=ListNode(0)
        curr=dummy
        for i in lis:
            dummy.next=ListNode(i)
            dummy=dummy.next
        dum=curr.next
        return dum