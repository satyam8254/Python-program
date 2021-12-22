n=int(input())
for i in range(n):
    s=input()
    if len(s)%3==0 and len(s)%5==0:
        print("foobar")
    elif len(s)%3==0:
        print("foo")
    elif len(s)%5==0:
            print("bar")
    else:
        print("-")
