def selectSwap(arr, n):

    minpos=arr.index(min(arr))
    maxpos=arr.index(max(arr))
    arr[minpos],arr[maxpos]=arr[maxpos],arr[minpos]
    return arr



if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*selectSwap(arr, n))


