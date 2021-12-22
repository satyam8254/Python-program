## Following function takes integer and should return True if it's prime 
## otherwise  should return False.
def is_prime(input_number):
    # You can start below this
    if input_number%2!=0 or input_number==2:
        return True
    elif input_number==1:
        return False
    else:
        return False



### Please don't change anything below this line.
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))