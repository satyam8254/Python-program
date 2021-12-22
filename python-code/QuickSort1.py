# Function to do Quick sort
def quickSort(arr, low, high):
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        quickSort(arr, 0, n-1)
        print(*arr)