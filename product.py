class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}")

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")