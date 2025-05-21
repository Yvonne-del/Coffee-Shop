from customer import Customer
from coffee import Coffee
from order import Order



# Create Customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create Orders
alice.create_order(latte, 4.0)
alice.create_order(latte, 5.0)
bob.create_order(latte, 6.0)
bob.create_order(espresso, 3.5)

# Customer tests
print("Alice's Orders:", alice.orders())
print("Alice's Coffees:", [coffee.coffee_name for coffee in alice.coffees()])

# Coffee tests
print("Latte Orders:", latte.orders())
print("Latte Customers:", [customer.customer_name for customer in latte.customers()])
print("Latte Total Orders:", latte.num_orders())
print("Latte Average Price:", latte.average_price())

# Test most_aficionado
top_customer = Customer.most_aficionado(latte)
if top_customer:
    print("Top spender on Latte:", top_customer.customer_name)
else:
    print("No orders for this coffee yet.")
