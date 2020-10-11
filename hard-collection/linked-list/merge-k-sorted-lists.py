import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        heapq.heapify(heap)
        
        for node in lists:
            if node is not None:
                heapq.heappush(heap, (node.val, node))
        
        head = point = ListNode(0)
        while len(heap) > 0:
            curr_val, curr_node = heapq.heappop(heap)
            point.next = curr_node
            point = point.next
            next_node = curr_node.next
            if next_node is not None:
                heapq.heappush(heap, (next_node.val, next_node))
        
        return head.next