from typing import Optional

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        lenA = 0
        currB = headB
        lenB = 0

        # Step 1: Calculate length of list A
        while currA is not None:
            lenA += 1
            currA = currA.next
        
        # Reset pointer
        currA = headA

        # Step 2: Calculate length of list B
        while currB is not None:
            lenB += 1
            currB = currB.next
        
        # Reset pointer
        currB = headB

        # Step 3: Align both pointers to same distance from end
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        # Step 4: Traverse together and find intersection
        while currA is not None:
            # 🔴 IMPORTANT: compare nodes, not values
            if currA == currB:
                return currA
            
            currA = currA.next
            currB = currB.next

        return None


# -------- MAIN --------
if __name__ == "__main__":
    # Create intersection part (shared nodes)
    intersect = ListNode(8)
    intersect.next = ListNode(10)

    # List A: 3 → 7 → 6 → 5 → 8 → 10
    headA = ListNode(3)
    headA.next = ListNode(7)
    headA.next.next = ListNode(6)
    headA.next.next.next = ListNode(5)
    headA.next.next.next.next = intersect

    # List B: 9 → 1 → 8 → 10
    headB = ListNode(9)
    headB.next = ListNode(1)
    headB.next.next = intersect

    sol = Solution()
    
    result = sol.getIntersectionNode(headA, headB)

    # 🔴 Print result properly
    if result:
        print("Intersection at node with value:", result.val)
    else:
        print("No intersection")