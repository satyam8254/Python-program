n= int(input())
male=[]
female=[]
for i in range(n):
    gender,talent=map(int,input().split())
    if gender==0:
        female.append(talent)
    elif gender==1:
        male.append(talent)
female.sort(reverse=True)
male.sort(reverse=True)
print(*(female+male))

