#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str_l1, str_l2 = '', ''
        while l1:            
            str_l1 += str(l1.val)
            l1 = l1.next
        while l2:            
            str_l2 += str(l2.val)
            l2 = l2.next
        int_l1 = int(str_l1[::-1])
        int_l2 = int(str_l2[::-1])       
        
        mylist = list(map(int, str(int_l1 + int_l2)[::-1]))
        
        tempnode = ListNode()
        headnode = tempnode
        for i,val in enumerate(mylist):
            if i == 0:
                tempnode.val = val
                continue
            tempnode.next = ListNode(val)
            tempnode = tempnode.next
        
        return headnode

def main():
    l1a = ListNode(2)
    l1b = ListNode(4)
    l1a.next = l1b
    l1c = ListNode(3)
    l1b.next = l1c
    l1c.next = None

    l2a = ListNode(5)
    l2b = ListNode(6)
    l2a.next = l2b
    l2c = ListNode(4)
    l2b.next = l2c
    l2c.next = None

    # ouput expected : [7,0,8] 
    s = Solution()
    out = s.addTwoNumbers(l1a,l2a)
    outlist = []
    while out:            
        outlist.append(out.val)
        out = out.next
    print(outlist)


if __name__ == "__main__":
    main()

# Runtime: 72 ms, faster than 20.31% of Python online submissions for Add Two Numbers.
# Memory Usage: 13.6 MB, less than 45.02% of Python online submissions for Add Two Numbers.