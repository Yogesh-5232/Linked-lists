def delNode(head, k):
    # Code here
    curr = head
    count = 1
    if head == None:
        return head
    if k == 1:
        return head.next
    while curr != None:
        if count == k-1:
            curr.next = curr.next.next
            return head
        count += 1
        curr = curr.next
    if k > count:
        return head
