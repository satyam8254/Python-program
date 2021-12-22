# Your class should be named `CarSell`.
# Your method should be named `getPromisingCustomers`
# Your method should return the indices of customers who are willing to pay greater than or equal to 90% of the car value
class CarSell:
    def __init__(self,customer_proposals):
        self.n=customer_proposals
    def getPromisingCustomers(self):
        l1=[]
        #self.n=[100,200,300]
        for i in range(len(self.n)):

            if self.n[i]>=900000:
                l1.append(i)
        
        if len(l1)==0:
            return [-1]
        return l1
        


if __name__ == "__main__":
    num_customers = int(input())
    customer_proposals = []
    for i in range(num_customers):
        customer_proposals.append(int(input()))

    car_sell = CarSell(customer_proposals)
    for j in car_sell.getPromisingCustomers():
        print(j)