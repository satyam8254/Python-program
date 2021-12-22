def coverUp(dist):
    if dist==0 or dist==1:
        return 1
    return coverUp(dist-1)+coverUp(dist-2)
for _ in range(int(input())):
    dist=int(input())
    print(coverUp(dist))