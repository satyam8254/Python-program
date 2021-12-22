## Following function takes integer and should return True if it's prime 
## otherwise  should return False.
def is_prime(input_number):
    # You can start below this
    if input_number==2:
        return True
    if input_number==0 or input_number==1:
        return False
    flag=True
    for i in range(2,input_number):
            if input_number%i==0:
                flag=False
                break
            else:
                flag=True
    if flag==False:
        return False
    else:
        return True
### Please don't change anything below this line.
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))