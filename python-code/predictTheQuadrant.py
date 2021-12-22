testCase = int(input())
for i in range(0,testCase):
    x, y = input().split()
    x=int(x)
    y=int(y)
    if x>0 and y>0:
      print("Q1")
    elif x<0 and y>0:
      print("Q2")
    elif x<0 and y<0:
      print("Q3")
    elif x>0 and y<0:
      print("Q4")
    else:
      print("0")