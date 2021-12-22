def recursiveSequence(n):
    if n==1:
        return 1
    term=1
    start=((n-1)*(n-1+1))//2+1
    end=start+n
    for i in range(start,end):
        term=term*i
    return recursiveSequence(n-1)+term

testCase = int(input())
for i in range(testCase):
    num=int(input())
    print(recursiveSequence(num))