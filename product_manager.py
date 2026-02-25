class ProductManager:
    def __init__(self):
        self.list_of_available_products = []
	

    def add_product(self, product):
        self.list_of_available_products.append(product)

    def display_products(self):
        print("List of products:")
        for product in self.list_of_available_products:
            product.display_info()

    def total_value(self):
        total = 0
        for product in self.list_of_available_products:
            total += product.price * product.quantity
        return total

    def remove_product(self, name):
        for p in self.list_of_available_products:
            if p.name == name:
                self.list_of_available_products.remove(p)
                return
        print("Product not found.")
