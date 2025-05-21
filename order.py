from customer import Customer
from coffee import Coffee
class Order:
    # class-level list to store all orders
    all_orders = []  


    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee 
        self.price = price
       
        Order.all_orders.append(self)

    #ensure all values of price are as required    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("price must be a float number between 1.0 and 10.0")

    #get values as attributes instead of mwthods
    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
    
    @classmethod
    def all(cls):
        return cls.all_orders
        