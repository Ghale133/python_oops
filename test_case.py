from burgerrr import Burger

def test_add_lettuce():
    burger = Burger()
    burger.add_lettuce()
    assert 'lettuce' in burger.ingredients
    assert burger.price == 170

def test_add_cheese():
    burger = Burger()
    burger.add_cheese()
    assert 'cheese' in burger.ingredients
    assert burger.price == 200

def test_add_tomatoes():
    burger = Burger()
    burger.add_tomatoes()
    assert 'tomatoes' in burger.ingredients
    assert burger.price == 160

def test_return_burger():
    burger = Burger()
    assert burger.return_burger() == burger.ingredients 

def test_return_price():
    burger = Burger()
    assert burger.return_price() == burger.price

