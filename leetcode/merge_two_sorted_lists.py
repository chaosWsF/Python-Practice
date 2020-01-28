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
        if not (l1 or l2):
            return None
        
        if not l1:
            return l2
        
        if not l2:
            return l1

        if l1.val <= l2.val:
            result = ListNode(l1.val)
            l1 = l1.next
        else:
            result = ListNode(l2.val)
            l2 = l2.next
        
        if l1 and l2:
            if l1.val <= l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next
            else:
                result.next = ListNode(l2.val)
                l2 = l2.next
        elif l1:
            result.next = l1
            return result
        elif l2:
            result.next = l2
            return result
        else:
            return result
        
        result_next = result.next
        while l1 and l2:
            if l1.val <= l2.val:
                result_next.next = ListNode(l1.val)
                l1 = l1.next
            else:
                result_next.next = ListNode(l2.val)
                l2 = l2.next
            
            result_next = result_next.next
        
        if l1:
            result_next.next = l1

        if l2:
            result_next.next = l2

        return result


def list2Linked(l):
    cur = dummy = ListNode(0)
    for e in l:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


def linked2List(ll):
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
    l1 = list2Linked(input_values[0])
    l2 = list2Linked(input_values[1])

    sol = Solution()
    t0 = perf_counter()
    l1_l2_merged = sol.mergeTwoLists(l1, l2)
    t1 = perf_counter()
    used_t = (t1 - t0) * 1e6

    print(linked2List(l1_l2_merged))
    print('Used time: {0:.3f} μs'.format(used_t))
