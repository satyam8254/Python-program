def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        s=n-i
        print(" "*s+"#"*i)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)