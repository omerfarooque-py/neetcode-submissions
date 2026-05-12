class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied_list = {None : None}
        curr = head
        while curr:
            new_node = Node(curr.val)
            copied_list[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            copy = copied_list[curr]
            copy.next = copied_list[curr.next]
            copy.random = copied_list[curr.random]
            curr = curr.next
        return copied_list[head]