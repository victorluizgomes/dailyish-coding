'''
You run an e-commerce website and want to record the last N order
ids in a log. Implement a data structure to accomplish this, with
the following API:

 - record(order_id): adds the order_id to the log

 - get_last(i): gets the ith last element from the log.
    i is guaranteed to be smaller than or equal to N.

'''

class Order_ids:
    
    def __init__(self, n):
        self.orders = []
        self.n = n

    # if the lenght of the orders list is greater than n number of ids pop
    # the oldest element in the list
    def record(self, order_id):
        self.orders.append(order_id)
        if len(self.orders) > self.n:
            self.orders.pop(0)

    def get_last(self, i):
        if i - 1 > len(self.orders):
            return None
        return self.orders[i - 1]

    def __str__(self):
        return str(self.orders)


order = Order_ids(5) # N = 5
order.record(10)
order.record(20)
print(order.get_last(5)) # None
order.record(30)
order.record(40)
order.record(50)
print(order.get_last(5)) # 50
order.record(60)
print(order.get_last(5)) # 60
print(order) # [20, 30, 40, 50, 60]
