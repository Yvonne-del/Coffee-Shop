from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
o1 = alice.create_order(latte, 4.0)
o2 = alice.create_order(latte, 5.0)
o3 = bob.create_order(latte, 6.0)
o4 = bob.create_order(espresso, 3.5)

# Test relationships
print("Alice's Orders:", alice.orders())         # Should show 2 orders
print("Alice's Coffees:", [c.name for c in alice.coffees()])  # ['Latte']

print("Latte's Orders:", latte.orders())         # 3 orders
print("Latte's Customers:", [c.name for c in latte.customers()])  # ['Alice', 'Bob']

print("Latte total orders:", latte.num_orders())  # 3
print("Latte average price:", latte.average_price())  # 5.0

# Test most aficionado
top_customer = Customer.most_aficionado(latte)
print("Top spender on Latte:", top_customer.name if top_customer else "None")
