def codeWord(word):
    morseCode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    res=set()
    for i in word:
        morse=""
        for j in i:
            code=morseCode[letters.index(j)]
            morse=morse+code
        res.add(morse)
    return len(res)
n=int(input())
for i in range(n):
    word=input().split()
    print(codeWord(word))