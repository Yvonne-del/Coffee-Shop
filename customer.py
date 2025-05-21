

class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name

        
    @property
    def name(self):
        return self._customer_name
    
    @name.setter
    def name(self, customer_name):
        if isinstance(customer_name, str) and 1 < len(customer_name) <= 15:
            self._customer_name = customer_name
        else:
            raise ValueError("Name must be a string  with a maximum number of 15 characters")
    
    def orders(self):
        from order import Order
        # Return all orders where this customer is the one in the order
        return [order for order in Order.all() if order.customer == self]
    
    def coffees(self):
        # Return unique Coffee instances this customer has ordered
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from order import Order 
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order

        # Filter orders for the given coffee
        orders = [order for order in Order.all() if order.coffee == coffee]

        if not orders:
            return None

        # Track total spending per customer
        spending = {}

        for order in orders:
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price

        # Find the customer who spent the most
        return max(spending, key=spending.get)
