"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes 
of the first two lists.

Example:

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""

from time import perf_counter

class ListNode:
    """singly-linked list"""
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """direct solution"""
        result_next = result = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                result_next.next = ListNode(l1.val)
                l1 = l1.next
            else:
                result_next.next = ListNode(l2.val)
                l2 = l2.next
            
            result_next = result_next.next

        result_next.next = l1 or l2

        return result.next

    def mergeTwoLists1(self, list1, list2):
        "recursively"
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val < list2.val:
            return ListNode(val=list1.val, next=self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(val=list2.val, next=self.mergeTwoLists(list1, list2.next))
    
    def mergeTwoLists2(self, l1, l2):
        """change into list"""
        l1 = linked2List(l1)
        l2 = linked2List(l2)
        result = sorted(l1 + l2)
        return list2Linked(result)


def list2Linked(l):
    cur = ll = ListNode(0)
    for e in l:
        cur.next = ListNode(e)
        cur = cur.next
    return ll.next

def linked2List(ll):
    if not ll:
        return []
    l = []
    while ll.next is not None:
        l.append(ll.val)
        ll = ll.next
    l.append(ll.val)
    return l


if __name__ == "__main__":

    input_values = [
        [1, 2, 4],
        [1, 3, 4]
    ]
    # input_values = [
    #     [],
    #     []
    # ]

    l1 = list2Linked(input_values[0])
    l2 = list2Linked(input_values[1])
    sol = Solution()
    t0 = perf_counter()

    l1_l2_merged = sol.mergeTwoLists(l1, l2)

    t1 = perf_counter()
    used_t = (t1 - t0) * 1e6
    print(linked2List(l1_l2_merged))
    print('Used time: {0:.3f} μs'.format(used_t))
