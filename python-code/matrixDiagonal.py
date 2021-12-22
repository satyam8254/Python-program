# name your function as change_diagonal and it should take list as input
def change_diagonal(mtx):
    for i in range(len(mtx)):
        j=i
        if mtx[i][j]<0:
            mtx[i][j]=0
        else:
            mtx[i][j]=1
    return mtx
# Do not change anything below this line.
if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])
    out = change_diagonal(lst)
    for lst1 in out:
        print(" ".join(str(i) for i in lst1))
        