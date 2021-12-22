from collections import Counter
number_Of_Shoes=int(input())
available_size=Counter(map(int,input().split()))
number_of_customer=int(input())
earning=0
for i in range(number_of_customer):
    size,price=map(int,input().split())
    if size in available_size and available_size[size]>0:
        available_size[size]-=1
        earning+=price
print(earning)
