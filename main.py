from product_manager import ProductManager
from product import Product
from cart import Cart
import random

manager = ProductManager()

p1 = Product("Laptop", 1200, 1)
p2 = Product("Mouse", 25, 10)
p3 = Product("Keyboard", 45, 5)
p4 = Product("Monitor", 300, 2)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)

manager.display_products()
print("Total value of inventory:", manager.total_value())

cart = Cart()

random_products = random.sample(manager.list_of_products, 3)

for product in random_products:
    cart.add_product_in_cart(product)
    
cart.display_cart_items()

print("Total value of cart:", cart.cart_value())
