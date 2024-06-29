# test_order.py


# Unit Tests
# • Test order __init__()
# o Assert order should include an empty list of pizza objects
# o Assert order should have a zero cost until an order is input
# o Assert order should not have yet been paid
# • Test order __str__()
# o Test order should return a string containing customer full order and cost
# • Test order input_pizza()
# o Test method should update cost
# • Test order order_paid()
# o Test method should update paid to true
# • Test pizza __init__()
# • Test return an initialized pizz


import pytest

from src.order import Order


@pytest.fixture
def my_order():    
    order = Order()
    return order

def test_order_init():
    """
    This method ensures that our initization 
    follows the rules intended by our order class 
    for objects upon initalization
    """
    
    my_order = Order()
    assert my_order.pizzas==[]              # compare to an empty list
    
    assert my_order.total_cost == 0.00      # nothing ordered yet!
    
    assert my_order.paid is not True        # not paid yet    


def test_order_paid(my_order):
    assert my_order.order_paid() == True
    
def test_str(my_order):                             # Test order __str__()
    assert type(my_order.__str__()) is str          # make sure it returns string type

#Test order should return a string containing customer full order and cost    
def test_fullorder(my_order):         
    assert len(my_order.__str__()) > 0              # must return full order
    
# Test method should update cost
def test_input_pizza(my_order):
    # create a pizza and check cost > 0
    my_order.input_pizza("Thin", ["Pesto"], "Mozzarella", ["Mushrooms"])   
    assert my_order.total_cost > 0.00


@pytest.mark.order
def test_all():    
    my_order = Order()
    test_order_init()
    test_order_paid(my_order)
    test_str(my_order)
    test_fullorder(my_order)
    test_input_pizza(my_order)
    
