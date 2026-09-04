from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    A = list1
    B = list2

    res = ListNode()
    tail = res

    while A and B:
        if A.val <= B.val:
            tail.next = A
            A = A.next
        else:
            tail.next = B
            B = B.next
        tail = tail.next

    tail.next = A if A else B
    return res.next


list1 = ListNode()
tail = list1
for _ in (1, 2, 4):
    temp = ListNode(_)
    tail.next = temp
    tail = tail.next


list2 = ListNode()
tail = list2
for _ in (1, 3, 4):
    temp = ListNode(_)
    tail.next = temp
    tail = tail.next

tail = None

tail = mergeTwoLists(list1.next, list2.next)

while tail:
    print(tail.val, end=" -> ")
    tail = tail.next
print("None")
