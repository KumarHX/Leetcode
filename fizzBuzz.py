class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        values = []
        while(n != 0):
            if(n % 3 == 0 and n % 5 == 0):
                values.append("FizzBuzz")
            elif(n % 3 == 0):
                values.append("Fizz")
            elif(n % 5 == 0):
                values.append("Buzz")
            else:
                values.append(str(n))
            n = n-1
        return values[::-1]