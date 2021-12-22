def factorial(n):
    # Implement this function
    if n<0:
        return("undefined")
    elif n==0 or n==1:
        return 1
    else:
        n=n*factorial(n-1)
        return n
# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    print(factorial(n))