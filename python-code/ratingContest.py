score = int(input())
if score < 1200 :
    print("ABC")
elif score > 1199 and score < 2800 :
    print("ARC")
elif score > 2799 :
    print("AGC")
else:
    print("non rating")