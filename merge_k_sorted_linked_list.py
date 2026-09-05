# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    def mergeLists(list1: Optional[ListNode], list2: Optional[ListNode]):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = mergeLists(list1.next, list2)
            return list1
        else:
            list2.next = mergeLists(list1, list2.next)
            return list2

    head = lists[0]
    for i in range(1, len(lists)):
        head = mergeLists(head, lists[i])

    return head
