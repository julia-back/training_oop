def test_product_init_tomato(product_obj_tomato):
    assert product_obj_tomato.name == "Помидор"
    assert product_obj_tomato.description == "Синьор Помидор"
    assert product_obj_tomato.price == 150.00
    assert product_obj_tomato.quantity == 5


def test_product_init_cucumber(product_obj_cucumber):
    assert product_obj_cucumber.name == "Огурец"
    assert product_obj_cucumber.description == "Мистер Кукумбер"
    assert product_obj_cucumber.price == 120.00
    assert product_obj_cucumber.quantity == 3
