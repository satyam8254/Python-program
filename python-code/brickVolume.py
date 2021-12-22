# You should fill this functions using the volume and calculate_price functions defined below this.
# dimensions is a list with 2 values width and height respectively
# brick_count is int representing total bricks
# def calculate_total_price_of_bricks(dimensions, brick_count):
#     for i in range(len(dimensions)):
#         length=100
#         if dimensions[0]==-1:
#             dimensions[0]=60
#         elif dimensions[1]==-1:
#             dimensions[1]=40
#         else:
#             brickVolume=length*dimensions[0]*dimensions[1]
#     price=0.00005
#     brickValue=brickVolume*price
#     brick_count=round(brick_count*brickValue)
#     return brick_count
def calculate_total_price_of_bricks(dimensions, brick_count):
    length=100
    width=60
    height=40
    if(dimensions[0]!=-1):
        width=dimensions[0]
    if (dimensions[1]!=-1):
        height=dimensions[1]
    total_vol=brick_count*volume(length,width,height)
    return calculate_price(total_vol)

### Do not change anything below this line
def volume(length=100,width=60,height=40):
	return length*width*height

def calculate_price(volume, price=0.00005):
	return round(volume*price)

if __name__ == "__main__":
    brick_count = int(input())
    dimensions = [int(i) for i in input().split(' ')]
    total_price = calculate_total_price_of_bricks(dimensions, brick_count)
    print(total_price)