# ===============================================
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         dummy = cur = ListNode(0)
#         carry = 0
#         while l1 or l2 or carry:
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
#             if l2:
#                 carry += l2.val
#                 l2 = l2.next
#             cur.next = ListNode(carry%10)
#             cur = cur.next
#             carry //= 10
#         return dummy.next
# ===============================================

class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        l1, l2 = convertLinkedList(l1), convertLinkedList(l2)
        l1, l2 = equalLen(l1, l2)
        result = list(map(lambda x: x[0] + x[1], zip(l1, l2)))
        if len(result) > 1:
            for i in range(len(result)):
                if result[i] > 9:
                    result[i] = result[i] - 10
                    if i < len(result) - 1:
                        result[i + 1] = result[i + 1] + 1
                    else:
                        result.append(1)
        else:
            if result[0] > 9:
                    result[0] = result[0] - 10
                    result.append(1)
        
        return result


def convertLinkedList(ll):
    l = []
    while ll.next is not None:
        l.append(ll.val)
        ll = ll.next
    
    l.append(ll.val)
    
    return l


def equalLen(l1, l2):
    if len(l1) > len(l2):
        return l1, l2 + ([0] * (len(l1)-len(l2)))
    elif len(l1) < len(l2):
        return l1 + ([0] * (len(l2)-len(l1))), l2
    else:
        return l1, l2


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


if __name__ == '__main__':
    input1 = [1]
    input2 = [9, 9]
    sol = Solution()

    input1 = lst2link(input1)
    input2 = lst2link(input2)

    output = sol.addTwoNumbers(input1, input2)
    print(output)
    # print(lst2link(output))