### Define the required class here...


class Rectangle:
    # Your code goes here
    def calculatePerimeter(self,l,w):
        self.l=l
        self.w=w
        


### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    l, w = map(int, input().split())
    r1 = Rectangle(l, w)
    print(r1.calculatePerimeter())