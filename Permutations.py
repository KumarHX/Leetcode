class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def bfs(self,num,val,res,used):
        if len(val)==len(num) and val not in res:
            res.append(val)
        for i in range(len(num)):
            if used[i]==False:
                used[i]=True
                val=val+[num[i]]
                self.bfs(num,val,res,used)
                val=val[:len(val)-1]
                used[i]=False
    def permute(self, num):
        res=[]
        if len(num)==0:
            return res
        used=[False]*len(num)
        self.bfs(num,[],res,used)
        return res

original: [1,2,3]


used: [True, False, False]
yo: [1]
used: [True, True, False]
yo: [1, 2]
used: [True, True, True]
yo: [1, 2, 3]
A: [1, 2, 3]
recursion stops
remove last element

[1, 2]
new used: [True, True, False]
A: [1, 2]
[1]
new used: [True, False, False]
used: [True, False, True]
yo: [1, 3]
used: [True, True, True]
yo: [1, 3, 2]
A: [1, 3, 2]


[1, 3]
new used: [True, False, True]
A: [1, 3]
[1]
new used: [True, False, False]
A: [1]
[]
new used: [False, False, False]
used: [False, True, False]
yo: [2]
used: [True, True, False]
yo: [2, 1]
used: [True, True, True]
yo: [2, 1, 3]
A: [2, 1, 3]


[2, 1]
new used: [True, True, False]
A: [2, 1]
[2]
new used: [False, True, False]
used: [False, True, True]
yo: [2, 3]
used: [True, True, True]
yo: [2, 3, 1]
A: [2, 3, 1]


[2, 3]
new used: [False, True, True]
A: [2, 3]
[2]
new used: [False, True, False]
A: [2]
[]
new used: [False, False, False]
used: [False, False, True]
yo: [3]
used: [True, False, True]
yo: [3, 1]
used: [True, True, True]
yo: [3, 1, 2]
A: [3, 1, 2]


[3, 1]
new used: [True, False, True]
A: [3, 1]
[3]
new used: [False, False, True]
used: [False, True, True]
yo: [3, 2]
used: [True, True, True]
yo: [3, 2, 1]
A: [3, 2, 1]


[3, 2]
new used: [False, True, True]
A: [3, 2]
[3]
new used: [False, False, True]
A: [3]
[]
new used: [False, False, False]
        