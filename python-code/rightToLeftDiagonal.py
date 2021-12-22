# name your function as right_to_left_diagonal
def  right_to_left_diagonal(num):
    a=[]
    for i in range(len(num)):
        j=len(num)-1-i
        a.append(num[i][j])
    return a


# Do not change anything below this line
if __name__ == "__main__":
    m = int(input())
    lst = []    
    for val in range(0, m):
        lst.append([int(i) for i in input().split(' ')])
    out = right_to_left_diagonal(lst)
    [print(val) for val in out]