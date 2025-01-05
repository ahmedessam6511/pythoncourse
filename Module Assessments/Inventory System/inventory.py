class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        print(f"Product Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity += amount
        print(f"Updated quantity of '{self.name}' to {self.quantity}")

    def calculate_total_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added product '{product.name}' to the inventory.")

    def display_inventory(self):
        if not self.products:
            print("The inventory is empty.")
        else:
            for product in self.products:
                product.display_product_info()

    def calculate_inventory_value(self):
        total_value = sum(product.calculate_total_value() for product in self.products)
        print(f"Total inventory value: ${total_value:.2f}")


inventory = Inventory()

inventory.add_product(Product("Laptop", 1200.00, 5))
inventory.add_product(Product("Smartphone", 800.00, 10))
inventory.add_product(Product("Headphones", 150.00, 20))

print("\nDisplaying inventory:")
inventory.display_inventory()

print("\nUpdating quantities:")
inventory.products[0].update_quantity(3)  
inventory.products[1].update_quantity(-2)  
print("\nDisplaying inventory after updates:")
inventory.display_inventory()

print("\nCalculating total inventory value:")
inventory.calculate_inventory_value()