# test_integration.py
#Test that code can handle multiple pizza objects per order
#o Ensure multiple pizza objects within a given order result in an additively larger cost


import pytest

from src.pizza import Pizza
from src.order import Order


def test_orders():
    """
    This method ensures that multiple pizza objects within a 
    given order result in an additively larger cost.
    
    We have 11, 11 and 18 for cost for the following orders.  
    
    Therefore total should be 40.00
    """
    my_order =  Order()   
    my_order.input_pizza("Thin", ["Pesto"], "Mozzarella", ["Mushrooms"])   
    assert my_order.total_cost == 11.00        
    
    my_order.input_pizza("Gluten_Free", ["Marinara"], "Mozzarella", ["Pineapple"])
    assert my_order.total_cost == 22.00                     # additive  -- includes perevious order

    my_order.input_pizza("Thin", ["Liv_Sauce", "Pesto"], "Mozzarella", ["Mushrooms", "Pepperoni"])
    assert my_order.total_cost == 40.00
    
