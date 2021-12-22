'''import array as arr
arr = []
sum = 0
marksOfNstudent = int(input())
for i in range(0,marksOfNstudent):
    value =int(input())
    arr.append(value)
    #print(arr)
for j in range(0,len(arr)):
    sum = sum + arr[j]
    #print(sum)
mean = sum / marksOfNstudent
print(int(mean))'''
import array as arr
n = int(input())
if (n>=1 and n<=n):
    arr = list(int(input().split()))
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
        mean = sum / n
        print(mean)
