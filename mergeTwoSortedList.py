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
        rlistH = ListNode()
        rlist = ListNode()

        #Check if L1 is empty
        if list1 is None:
            #Check if L2 is empty
            if list2 is None:
                #Both are empty
                return list1
            else:
                #List 1 is empty return list 2
                return list2
        elif list2 is None:
            #Only list 2 is empty so return list 1
            return list1
        # We know there is something in both lists
        elif list1.val <= list2.val:
            rlistH.val = list1.val
            
            #Check if l1 has next
            if list1.next is None:
                #If it doesnt attach list2 to the end rlistH and return the head
                rlistH.next = list2
                return rlistH
            else:
                #Else set the next item in the list
                list1 = list1.next
            
        elif list1.val > list2.val:
            rlistH.val = list2.val

            #Check if l2 has next
            if list2.next is None:
                #Attach the rest of L1 to rlistH and return
                rlistH.next = list1
                return rlistH
            else:
                list2 = list2.next

        #From here we have set the head and can start organizing the rest of the list
        rlistH.next = rlist
        while True:
            if list1.val < list2.val:
                rlist.val=list1.val
                
                if list1.next is None:
                    rlist.next = list2
                    return rlistH
                else:
                    rlist.next = ListNode()
                    rlist = rlist.next
                    list1 = list1.next
            else:
                rlist.val = list2.val

                if list2.next is None:
                    rlist.next = list1
                    return rlistH
                else:
                    rlist.next = ListNode()
                    rlist = rlist.next
                    list2 = list2.next


class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next