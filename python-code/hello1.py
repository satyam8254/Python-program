                                 #time,space
n = int(input())                    #1,1
for i in range(n):                  #n,0
    j = 1                           #1,1
    while(j<n):                   #n*n,0
        print("hello")              #1,0
        j *= 2                      #1,1

#O(1*4)+O(n)+O(n*n)
# time complexity = O(n log n)

#1*3
# space complexity = O(1)