class Product:
    def __init__(self, name: str, price: float = 0.0) -> None:
        self.name = name
        self.price = price

    def total_price(self, quantity: float = 1.0) -> float:
        return round(self.price * quantity, 2)


class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.quantity = []

    def add_to_cart(self, item: Product, quantity: float = 0.0) -> None:
        if item in self.products:
            self.quantity[self.products.index(item)] += quantity
        else:
            self.products.append(item)
            self.quantity.append(quantity)

    def total_price(self) -> float:
        price = 0.0
        for item, quantity in zip(self.products, self.quantity):
            price += item.total_price(quantity)
        return round(price, 2)

    def product_list(self) -> None:
        print("Products in cart:")
        for item, quantity in zip(self.products, self.quantity):
            print(f'{item.name} -- ${item.price} -- {quantity}')


if __name__ == "__main__":
    ...
