# Write function with name sum_of_multiples which takes a list and integer
# It should return sum of multiple of integer given.
# You can start from here
import math
def sum_of_multiples(numbers, mult):
    odd=0
    for i in range(len(numbers)):
        if numbers[i]%mult==0:
            odd=odd+numbers[i]
    return odd

	
# Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    mult = int(input())
    print(sum_of_multiples(numbers, mult))