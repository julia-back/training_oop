from src.product import Product


class Category:
    name: str
    description: str
    products: list
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        products_count = 0
        for product in self.__products:
            products_count += product.quantity
        return f"{self.name}, количество продуктов: {products_count} шт."

    @property
    def products(self):
        products = ""
        for product in self.__products:
            p = f"{product}\n"
            products += p
        return products

    def add_product(self, product_to_add: Product):
        self.__products.append(product_to_add)
        Category.product_count += 1
