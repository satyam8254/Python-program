# Write a function with name even_odd_separator, you should exactly the same name
# This even_odd_separator functions should take a list of integers and return a list
# you can start from here	
def even_odd_separator(numbers):
    list1=[]
    list2=[]
    list3=[]
    for i in range(len(numbers)):
        if numbers[i]%2==1:
            list1.append(numbers[i])
        elif numbers[i]%2==0:
            list2.append(numbers[i])
    list3=list1+list2
    return list3
### Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    separated = even_odd_separator(numbers)
    for num in separated:
    	print(num)