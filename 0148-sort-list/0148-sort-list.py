# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        n=0
        k=[]
        curr=head
        while curr:
            n+=1
            k.append(curr.val)
            curr=curr.next
        k=sorted(k)
        curr=head
        i=0
        while curr and i<len(k):
            curr.val=k[i]
            i+=1
            curr=curr.next
        return head

        