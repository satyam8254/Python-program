# Your class should be named `CarSell`.
# Your method should be named `getPromisingCustomers`
# Your method should return the indices of customers who are willing to pay greater than or equal to 90% of the car value
class CarSell:
    def __init__(self,noOfCustomer):
        self.noOfCustomer=noOfCustomer
    def getPromisingCustomers(self):
        priceValue=1000000*0.90
        list1=[]
        for i in range(len(self.noOfCustomer)):
            if self.noOfCustomer[i]>=priceValue:
                list1.append(i)
                pass
        if len(list1)>0:
            return list1
        else:
            return [-1]

if __name__ == "__main__":
    num_customers = int(input())
    customer_proposals = []
    for i in range(num_customers):
        customer_proposals.append(int(input()))
    car_sell = CarSell(customer_proposals)
    for j in car_sell.getPromisingCustomers():
        print(j)