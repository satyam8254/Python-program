## This function should return single integer. The integer should be maximum value of input list
## Please fill the following function
def maximum_value(input_numbers):
    # write below this here
    mx=max(input_numbers)
    return mx


## This function should return single integer. 
## The integer should be minimum value of input list
def minimum_value(input_numbers):
    # Please write below this
    mn=min(input_numbers)
    return mn


## This function should return list of integer which lies between m1 and m2. 
## if m1 <= m2 return list off numbers between m1 and m2
## if m2 <= m1 return list off numbers between m2 and m1
def get_numbers_in_range(input_numbers, m1, m2):
    # Please write below this line
    arr=[]
    if m1<=m2:
        for i in input_numbers:
            if i>=m1 and i<=m2:
                arr.append(i)
        #return (arr)
    elif m1>=m2:
        for i in input_numbers:
            if i>=m2 and i<=m1:
                arr.append(i)
        #return arr
    if len(arr)==0:
        return(-1)
    else:
        return(arr)
        
### Please do not change anything below this line.
if __name__ == "__main__":
    list1 = [int(i) for i in input().split(' ')]
    list2 = [int(i) for i in input().split(' ')]
    list3 = [int(i) for i in input().split(' ')]
    m1 = minimum_value(list1)
    m2 = maximum_value(list2)
    min_max_range = get_numbers_in_range(list3, m1, m2)
    [print(i) for i in min_max_range]