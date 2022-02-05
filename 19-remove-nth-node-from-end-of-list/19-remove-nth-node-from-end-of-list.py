class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        for _ in range(n):
            node2 = node2.next

        node_prev = None
        while node2:
            node_prev = node1
            node1 = node1.next
            node2 = node2.next

        if node_prev is None:
            return head.next

        node_prev.next = node1.next
        return head
        