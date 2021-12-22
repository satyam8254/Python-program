from collections import defaultdict
def CountingStars(string,size):
    d=defaultdict(int)
    res=0
    for i in string:
        res=res+d[i]
        d[i]=d[i]+1
    return res
tc=int(input())
for i in range(tc):
    size=int(input())
    string=input()
    print(CountingStars(string,size))


























# t=int(input())
# for i in range(t):
#     size=int(input())
#     string=input()[:size]
# s1=""
# cnt=0
# for i in string:
#     if i in s1:
#         cnt=cnt+s1.count(i)
#     else:
#         cnt=cnt+0
#     s1=s1+i
# print(cnt)


#using dictionary

# n=int(input())
# sum = 0
# d={}
# for i in range(n):
#     s=int(input())
#     a=input()
#     if a in d:
#         d[a]+=1
#     else:
#         d[a]=0
#     sum += d[a]
# #print(sum)
# for values in  d.items():
#     print(str(values))













# noftest = int(input())
# for i in range(noftest):
#     nofstars = int(input())
#     string = input()
#     dstars = {}
#     for ele in string:
#         if ele in dstars:
#             dstars[ele] = dstars[ele] + 1
#         else:
#             dstars[ele] = 0
#     su = 0
#     for key , value in dstars.items():
#         su = su + value
#     print(su)