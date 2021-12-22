if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr=set(arr)
mx=max(arr)
arr.remove(mx)
secmax=max(arr)
print(sec)