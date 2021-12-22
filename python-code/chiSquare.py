from collections import Counter
tc= int(input())
for i in range(tc):
   s = input()
   def is_palindrome(s):
       d = dict(Counter(s))
       odd = 0
       for i in d:
           if d[i]%2!=0:
               odd = odd + 1
       ans = "no"
       if len(s)%2!=0:
           if odd ==1:
               ans = "yes"
       else:
           if odd == 0:
               ans="yes"
       return ans
   d = dict(Counter(s))
   odd = 0
   for i in d:
       if d[i]%2!=0:
           odd = odd + 1
   if is_palindrome(s)=="yes":
       print(0)
   else:
       print(odd-1)