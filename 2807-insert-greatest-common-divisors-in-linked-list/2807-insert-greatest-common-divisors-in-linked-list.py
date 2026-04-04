# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getgcd(a,b):
            while b:
                a,b=b,a%b
            return abs(a)
        curr1=head
        curr2=head.next
        arr=[]
        while curr1 and curr2:
            arr.append(curr1.val)
            arr.append(getgcd(curr1.val,curr2.val))
            curr1=curr1.next
            curr2=curr2.next
        arr.append(curr1.val)        
        dummy=ListNode(0)
        k=dummy
        for i in arr:
            k.next=ListNode(i)
            k=k.next
        return dummy.next