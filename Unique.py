class Solution:
    def rd(self,n):
        if not n:
            return 0
        k=1
        for i in range(1,len(n)):
            if n[i] != n[i-1]:
                n[k] = n[i]
                k += 1
        return k
s=Solution()
r=s.rd([1,1,2,3,4,5,3])

print(r)
