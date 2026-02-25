class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product_in_cart(self, product):
        self.cart_items.append(product)

    def cart_value(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        return total

    def display_cart_items(self):
        print("List of products in cart:")
        for product in self.cart_items:
            product.display_info()