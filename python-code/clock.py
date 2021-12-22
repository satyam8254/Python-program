num1,num2 = map(int,input().split())
time =num1 + num2
if time<= 12:
    print(time)
elif time <=23:
    print(time-12)
elif time%12==0 or time>=24:
    print("12")

