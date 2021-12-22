class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root=num**0.5
        if root*root==num:
            print("true")
            return("true")
            
        else:
            print("false")
            return("false")
    num=int(input())
    isPerfectSquare(1,num)