class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        
        Sum of two bits can be obtained by performing XOR (^) of the two bits. 
        Carry bit can be obtained by performing AND (&) of two bits.
        Above is simple Half Adder logic that can be used to add 2 single bits. 
        We can extend this logic for integers. 
        If x and y don’t have set bits at same position(s), then bitwise XOR (^) of x and y gives the sum of x and y. 
        To incorporate common set bits also, bitwise AND (&) is used. 
        Bitwise AND of x and y gives all carry bits. We calculate (x & y) << 1 and add it to x ^ y to get the required result.
        
        """
        
        MOD = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            a, b = (a ^ b) & MOD, ((a & b) << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        
        """
        
        return sum([a,b])