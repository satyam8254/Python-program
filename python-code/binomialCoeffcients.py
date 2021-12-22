def binomialCoeff(n, r):
    # Implement this function
    if r==0 or n==r:
        return 1
    return binomialCoeff(n-1,r-1)+binomialCoeff(n-1,r)

# Do not edit anything below
if __name__ == "__main__":
    numTcs = int(input())
    for index in range(numTcs):
        inputInts = input().split(' ')
        n = int(inputInts[0])
        r = int(inputInts[1])
        print(binomialCoeff(n, r))