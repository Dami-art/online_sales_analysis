from product_manager import ProductManager
from product import Product

manager = ProductManager()

p1 = Product("Laptop", 1200, 1)
p2 = Product("Mouse", 25, 10)
p3 = Product("Keyboard", 45, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.display_products()
print("Total value of inventory:", manager.total_value())