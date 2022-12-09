class Product:
    def __init__(self, name: str, price: float = 0.0) -> None:
        self.name = name
        self.price = price

    def total_price(self, quantity: float = 1.0) -> float:
        return round(self.price * quantity, 2)


class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.products_quantity = []

    def add_to_cart(self, item, quantity: float = 0.0) -> None:
        item = [item.name, item.price]
        if item not in self.products:
            self.products.append(item)
            self.products_quantity.append(quantity)
        else:
            self.products_quantity[self.products.index(item)] += quantity

    def total_price(self) -> float:
        price = 0
        for product in self.products:
            price += product[1] * self.products_quantity[self.products.index(product)]
        return round(price, 2)

    def product_list(self) -> None:
        print("Products in cart:")
        for product in self.products:
            print(f'{product[0]} -- ${product[1]} -- {self.products_quantity[self.products.index(product)]}')


if __name__ == "__main__":
    ...
