from order import Order

class Coffee:
    def __init__(self, coffee_name):
        self.coffee_name = coffee_name

    
    @property
    def coffee_name(self):
        return self._coffee_name
    
    @coffee_name.setter
    def coffee_name(self, coffee_name):
        if isinstance(coffee_name, str) and len(coffee_name) >= 3:
            self._coffee_name = coffee_name
        else:
            raise ValueError("Name must be a string  with a minimum of 3 characters")
        
    def orders(self):
        return [order for order in Order.all() if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        all_orders = self.orders()
        if not all_orders:
            return 0 
        total_price = sum(order.price for order in all_orders)
        return total_price / len(all_orders)