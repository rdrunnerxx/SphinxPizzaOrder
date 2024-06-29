#Name: Mehdi (MED) Shakeri(mshakeri4@jh.edu)

#Module Info: Module 4 - Pytest and Sphinx, due 06/30/2024 at 11:59pm 

# An order must contain at least one pizza.

import pytest

from src.pizza import Pizza


    
# Class to store information about a Orders
class Order:
    """
     An extensible pizza ordering class: A service class to allow other 
     developers to quickly build upon restaurant template and extend to new 
     menu items and processes.
    """
    
    #assign a unique integer order id to each order
    def __init__(self):
        self.pizzas      = []
        self.total_cost  = 0.00                           # total cost of order (could be aggregate, multiple pizza orders)            
        self.paid        = False                          # false initially

    #=================================
    # Input the customers order for a given pizza
    # Initialize the pizza object and attach to the order
    # Update the cost            
    # Ensure multiple pizza objects within a given order result in an additively larger cost        
    def input_pizza(self, crust, sauce, cheese, toppings):
        my_pizza = Pizza(crust, sauce, cheese, toppings)        
        self.total_cost += my_pizza.price
        self.pizzas.append(my_pizza)
        return my_pizza
   
    #=================================
    # Print a customer's complete order
    def __str__(self)->str:
        
        s = ""
        for piz in self.pizzas:            
            s += (f"Crust: {piz.crust}, Sauce: {piz.sauce}, Cheese: {piz.cheese}, Toppings: {piz.toppings}, Cost: {piz.price}\n")
        s += (f"Total Cost: {self.total_cost}")            
        return s
    
    #=================================
    # Set Order as paid once payment has been collected
    def order_paid(self)->bool:
        self.paid = True
        return self.paid
    


   
        
        

