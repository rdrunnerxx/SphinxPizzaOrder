# test_pizza.py


# Unit Tests

#  Test pizza __init__()
#  Test return an initialized pizz


import pytest

from src.pizza import Pizza




@pytest.fixture
def my_pizza():    
    pizza = Pizza()
    return pizza



def test_pizza_init():
    """  
    Tests return an initialized pizza
    
    Test pizza should have crust (str), sauce (list of str), cheese
        (str), toppings (list of str)
        
    Test pizza should return a non-zero cost
    """
    
    my_pizza = Pizza("Thin", ["Pesto"], "Mozzarella", ["Mushrooms"])     
    
    assert my_pizza is not None                             # object cannot be NULL
    
    assert type(my_pizza.crust) is str                      # check type
    assert len(my_pizza.crust) > 0                          # then check not empty
    
    assert type(my_pizza.sauce) is list                     # check type      
    assert len(my_pizza.sauce) > 0                          # then check not empty

    assert type(my_pizza.cheese) is str                     # check type
    assert len(my_pizza.cheese) > 0                         # then check not empty          
    
    assert type(my_pizza.toppings) is list                  # check type
    assert len(my_pizza.toppings) > 0                       # then check not empty        

    assert my_pizza.crustprice > 0                          # a non-zero cost
    

@pytest.fixture
def my_new_pizza():
    """
    This method ensures that our pizza methods 
    follows the rules intended by our pizza class 
    for objects upon input of our new_pizza
    """
    pizza = Pizza("Thin", ["Pesto"], "Mozzarella", ["Mushrooms"])     
    return pizza

    
def test_cost(my_new_pizza):
    """
    In this method we evaluate cost of thin crust pizza.
    It should be 5.00
    """
    assert my_new_pizza.crustprice == 5.00                  # thin crust should be 5.00

#Test return of correct cost for an input pizz    
def test_str(my_new_pizza):                                 # Test pizza __str__()
    """
    In this method we make sure str method of object
    retuns a string value
    
    Test pizza should return a string containing the pizza and cost >0
    
    """
    assert type(my_new_pizza.__str__()) is str              # make sure it returns string type
    
    assert my_new_pizza.crustprice > 0                      # cost cannot be 0.00
    

@pytest.mark.pizza
def test_all():    
    my_pizza = Pizza("Thin", ["Pesto"], "Mozzarella", ["Mushrooms"]) 
    test_pizza_init()
    test_cost(my_pizza)
    test_str(my_pizza)
    