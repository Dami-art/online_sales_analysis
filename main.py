from product_manager import ProductManager
from product import Product
from cart import Cart
import random

manager = ProductManager()

p1 = Product("Gaming Laptop", 1200, 1)
p2 = Product("Mouse", 25, 11)
p3 = Product("Mechanical Keyboard", 45, 2)
p4 = Product("Monitor", 300, 22)

#p1.name = "Gaming Laptop"
#p2.quantity = 11
#p3.name = "Mechanical Keyboard"
#p4.quantity = 22

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)



cart = Cart()

random_products = random.sample(manager.list_of_products, 3)

for product in random_products:
    cart.add_product_in_cart(product)
    
cart.display_cart_items()

print("Total value of cart:", cart.cart_value())
