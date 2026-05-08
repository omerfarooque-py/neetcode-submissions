class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        prev = None

        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        curr = slow.next
        slow.next = None
        prev = None  

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        while prev:  
              tmp1 = head.next
              tmp2 = prev.next
              head.next = prev
              prev.next = tmp1
              head = tmp1
              prev = tmp2
        
        

        




         