# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rlist = []
        
        while True:
            if list1.value < list2.value:
                rlist.append(list1.value)
                if list1.next == None:
                    while True:
                        if list2.next != None:
                           rlist.append(list2.value)
                           list2 = list2.next
                        else:
                            rlist.append(list2.value)
                            return(rlist)
                else:
                    list1 = list1.next
            elif list1.value > list2.value:
                rlist.append(list2.value)
                if list2.next == None:
                    while True:
                        if list1.next != None:
                            rlist.append(list1.value)
                            list1 = list1.next
                        else