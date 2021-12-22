n=int(input())
arr=[int(x) for x in input().split()]
arr.sort(reverse=True)
arr.sort(key=lambda x:(str(x).count('2')),reverse=True)
print(*arr)
