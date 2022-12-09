class Product:
    def __init__(self, name: str, price: float = 0.0) -> None:
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product {self.name} with price ${self.price}."

    def total_price(self, quantity: float = 1.0) -> float:
        return round(self.price * quantity, 2)


class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.products_quantity = []

    def __repr__(self):
        return f"There are {len(self.products)} types of goods in the shopping cart."

    def _adding_func(self, item: object, quantity: float) -> None:
        if item not in self.products:
            self.products.append(item)
            self.products_quantity.append(quantity)
        else:
            self.products_quantity[self.products.index(item)] += quantity

    def add_to_cart(self, item: object, quantity: float = 0.0) -> None:
        if isinstance(item, Product):
            item = [item.name, item.price]
            self._adding_func(item, quantity)
        elif isinstance(item, ShoppingCart):
            for cart_item in item.products:
                cart_item_quantity = item.products_quantity[item.products.index(cart_item)]
                self._adding_func(cart_item, cart_item_quantity)

    def total_price(self) -> float:
        price = 0.0
        for product in self.products:
            price += product[1] * self.products_quantity[self.products.index(product)]
        return round(price, 2)

    def product_list(self) -> None:
        print("Products in cart:")
        for product in self.products:
            print(f'{product[0]} -- ${product[1]} -- {self.products_quantity[self.products.index(product)]}')


if __name__ == "__main__":
    ...
