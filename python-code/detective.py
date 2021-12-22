
import re
t=int(input())
for i in range(t):
    p = input().lower()
    q = input().lower()

    p =p.replace(" ","")
    q = q.replace(" ","")

    p = re.sub('[^a-z0-9]','',p)
    q= re.sub('[^a-z0-9]','',q)
    if sorted(p)==sorted(q):
        print('YES')
    else:
        print('NO')