from src.category import Category


def test_category(category_obj_vegetables):
    assert category_obj_vegetables.name == "Овощи"
    assert category_obj_vegetables.description == "Полезные штучки"
    assert len(category_obj_vegetables.products) == 2

    assert Category.category_count == 1
    assert category_obj_vegetables.category_count == 1
    assert Category.product_count == 2
    assert category_obj_vegetables.product_count == 2
