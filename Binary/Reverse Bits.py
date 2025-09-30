class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        j=0
        while n!=0:
            bit=n%2
            result += bit*(2**(31-j))
            n=n//2
            j+=1
        return result
