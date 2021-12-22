### Define the required class here...
import time
class Flight:
    def __init__(self, upTime, downTime):
        self.upTime = upTime
        self.downTime = downTime

    def calculateFlight(self):
        # Your Code goes here
        h1,m1=self.upTime.split(':')
        h2,m2=self.downTime.split(':')
        hr=(int(h2)-int(h1))*60
        mn=(int(m2)-int(m1))
        time=hr+mn
        return time

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    t1 = input()
    t2 = input()

    f1 = Flight(t1, t2)
    print(f1.calculateFlight())