class Solution:
    def compute(self,head):
        #Your code here
        S=[]
        while head:
            while S!=[] and S[-1].data<head.data:
                S.pop()
            S.append(head)
            head=head.next
        S.append(None)
        for i in range(len(S)-1):
            S[i].next=S[i+1]
        return S[0]
