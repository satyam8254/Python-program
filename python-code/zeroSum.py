def zeroSum(matrix, rows, cols):
    rc=0
    cc=0
    for i in range(rows):
        rowSum=0
        for j in range(cols):
            rowSum=rowSum+matrix[i][j]
        if rowSum==0:
            rc+=1
    for i in range(cols):
        colSum=0
        for j in range(rows):
            colSum=colSum+matrix[j][i]
        if colSum==0:
            cc+=1
    return rc+cc
for _ in range(int(input())):
    n,m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for i in range(n)]
    print(zeroSum(arr, n, m))



# def zeroSum(matrix, rows, cols):
#     rc=0
#     cc=0
#     for i in range(rows):
#         rowSum=0
#         colSum=0
#         for j in range(cols):
#             rowSum=rowSum+matrix[i][j]
#             colSum=colSum+matrix[j][i]
#         # print("row : - ",i,rowSum)
#         # print("col : -",i,colSum)
#         if rowSum==0:
#             rc+=1
#         # print("rc",rc)
#         if colSum==0:
#             cc+=1
#         # print("cc",cc)
#     return rc+cc
# for _ in range(int(input())):
#     n,m = map(int, input().split())
#     arr = [[int(x) for x in input().split()] for i in range(n)]
#     print(zeroSum(arr, n, m))





# def zeroSum(matrix, rows, cols):
#     summ=0
#     cont=0
#     for r in range(rows):
#         for c in range(len(matrix[0])):
#             summ+=matrix[r][c]
#         if summ==0:
#             cont+=1
#         summ=0
#     summ=0
#     for c in range(len(matrix[0])):
#         for r in range(rows):
#             summ+=matrix[r][c]
#         if summ==0:
#             cont+=1
#         summ=0
#     return cont
# for _ in range(int(input())):
#     n,m = map(int, input().split())
#     arr = [[int(x) for x in input().split()] for i in range(n)]
#     print(zeroSum(arr, n, m))