class Product:
    name: str
    description: str
    price: float
    quantity: int
    products_list: list = list()

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append({"name": name, "description": description,
                                      "price": price, "quantity": quantity})

    @classmethod
    def new_product(cls, product_param):
        """
        Принимает словарь с ключами: "name"(название), "description"(описание),
        "price"(цена), "quantity"(количество на складе)
        """
        name, description, price, quantity = product_param.values()
        for product in cls.products_list:
            for key, value in product.items():
                if key == "name" and value.lower() == name.lower():
                    product["quantity"] += quantity
                    if product["price"] < price:
                        product["price"] = price
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:
                agreement = input("Старая цена товара выше введенной.\n"
                                  "Вы уверены, что хотите снизить цену на товар?\n"
                                  "y - да / n - нет\n")
                if agreement.lower() == "y":
                    self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")
