# Read a string
s = input()
#  Declare variables to store count of vowels
a = 0
e = 0
i = 0
o = 0
u = 0
s_len = len(s)
#  Iterate over each character in the string
for j in range(s_len):
    #  Check for each character in if else
    if(s[j] == 'a'):
        a += 1
    elif(s[j] == 'e'):
        e += 1
    elif(s[j] == 'i'):
        i += 1
    elif(s[j] == 'o'):
        o += 1
    elif(s[j] == 'u'):
        u += 1
#  Print out the result
print("occurence of a is", a)
print("occurence of e is", e)
print("occurence of i is", i)
print("occurence of o is", o)
print("occurence of u is", u)