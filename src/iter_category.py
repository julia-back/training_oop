from src.category import Category


class IterProductsInCategory:
    pass

    def __init__(self, category: Category):
        products_list = category.products.split("\n")
        products_list.remove("")
        self.products_list = products_list
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.products_list):
            result = self.products_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
