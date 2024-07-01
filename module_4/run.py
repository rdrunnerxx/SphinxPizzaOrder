#Name: Mehdi (MED) Shakeri(mshakeri4@jh.edu)

#Module Info: Module 4 - Pytest and Sphinx, due 06/30/2024 at 11:59pm 
# use the following command to install on desktop and laptop folders
#C:\Users\Med.MED80\AppData\Local\Programs\Python\Python312\python -m pip install pytest
#C:\Users\MEDP71\AppData\Local\Programs\Python\Python312  -m pip install pytest OR Sphinx

# For Documentation See:
# https://sphinxpizzaorder.readthedocs.io/en/latest/index.html#

# An order must contain at least one pizza.

from src.order import Order



#=======================

if __name__ == "__main__":
    """
        This method is main point of starting app, and it orders 3 pizzas!
    """
    
    my_order = Order()                      # creates an order object
    
    # test for multiple orders
    my_order.input_pizza("Thin", ["Pesto"], "Mozzarella", ["Mushrooms"])    #create new pizzas
    my_order.input_pizza("Gluten_Free", ["Marinara"], "Mozzarella", ["Pineapple"])
    my_order.input_pizza("Thin", ["Liv_Sauce", "Pesto"], "Mozzarella", ["Mushrooms", "Pepperoni"])


    print(str(my_order))        
    
    
    
    


