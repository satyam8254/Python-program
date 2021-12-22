# Do not change the function signature
# Fill in the function 
# string_to_repeat will be string like 'abc'
# repeat will be an int like 3
# return 'abc abc abc'
def string_repeat(string_to_repeat, repeat):
    # Write from here
    string=string_to_repeat+ " "
    r=string*int(repeat)
    return r


string_repeat('abc',3)

# Please don't change anything below this line.
# You don't have to worry about reading input, just fill the function above.
if __name__ == "__main__":
    input_string = input()
    input_number = input()
    print(string_repeat(input_string, input_number))