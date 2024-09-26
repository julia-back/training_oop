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
        Product.products_list.append(self)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_param):
        """
        Принимает словарь с ключами: "name"(название), "description"(описание),
        "price"(цена), "quantity"(количество на складе)
        """
        name, description, price, quantity = product_param.values()
        for product in cls.products_list:
            if product.name.lower() == name.lower():
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:
                agreement = input(
                    "Старая цена товара выше введенной.\n"
                    "Вы уверены, что хотите снизить цену на товар?\n"
                    "y - да / n - нет\n"
                )
                if agreement.lower() != "y":
                    return
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError








