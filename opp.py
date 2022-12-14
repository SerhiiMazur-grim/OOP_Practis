class Product:
    def __init__(self, name: str, price: float = 0.0) -> None:
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}, {self.price}"

    def __eq__(self, another_prod):
        return self.name == another_prod.name and self.price == another.price

    def __float__(self) -> float:
        return self.price

    def __str__(self) -> str:
        return self.name

    def total_price(self, quantity: float = 1.0) -> float:
        return round(self.price * quantity, 2)


class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.quantity = []

    def __repr__(self) -> str:
        return f"{list(zip(self.products, self.quantity))}"

    def __float__(self):
        return self.total_price()

    def __iter__(self) -> iter:
        return zip(self.products, self.quantity)

    def add_to_cart(self, item: Product, quantity: float = 0.0) -> None:
        if item in self.products:
            self.quantity[self.products.index(item)] += quantity
        else:
            self.products.append(item)
            self.quantity.append(quantity)

    def __add__(self, prod_or_cart):
        new_cart = ShoppingCart()
        new_cart.products = self.products.copy()
        new_cart.quantity = self.quantity.copy()

        if isinstance(prod_or_cart, ShoppingCart):
            for prod, quan in prod_or_cart:
                new_cart.add_to_cart(prod, quan)
        elif isinstance(prod_or_cart, Product):
            new_cart.add_to_cart(prod_or_cart, 1)
        return new_cart

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
