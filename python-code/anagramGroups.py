from collections import defaultdict
def groupAnagrams(strs):
    group=defaultdict(list)
    for i in strs:
        group["".join(sorted(strs))].append(i)
    for j in group.value():
        print(" ".join(j))

if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        print(groupAnagrams(arr))