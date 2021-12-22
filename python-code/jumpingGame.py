def game(panel,i,jcount,pathLength):
    if i>=len(panel):
        pathLength.append(jcount)
        return
    game(panel,i+1,jcount+1,pathLength)
    game(panel,i+panel[i],jcount+1,pathLength)

n=int(input())
panel=[int(x) for x in input().split()[:n]]
pathLength=[]
game(panel,0,0,pathLength)
print(min(pathLength))
