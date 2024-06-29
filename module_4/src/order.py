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
     
     An order must contain at least one pizza.
    """
    
    #assign a unique integer order id to each order
    def __init__(self):

        """
        init method initializes pizza list of items to none
        total cost is set to 0.00 
        paid is set to false
        """
        self.pizzas      = []
        self.total_cost  = 0.00                           # total cost of order (could be aggregate, multiple pizza orders)            
        self.paid        = False                          # false initially

    #=================================
    # Input the customers order for a given pizza
    # Initialize the pizza object and attach to the order
    # Update the cost            
    # Ensure multiple pizza objects within a given order result in an additively larger cost        
    def input_pizza(self, crust, sauce, cheese, toppings):
        """
         Add a Pizza object to the Order
        
        :param: crust - The crust of the pizza. (a string)
        :param: sauce - The sauce of the pizza. (string lis)
        :param: cheese - The cheese of the pizza. (a string)
        :param: toppings - The toppings of the pizza. (string list)
        
        :return: The pizza object that is created
        
        """

        my_pizza = Pizza(crust, sauce, cheese, toppings)        
        self.total_cost += my_pizza.price
        self.pizzas.append(my_pizza)
        return my_pizza
   
    #=================================
    # Print a customer's complete order
    def __str__(self)->str:
        """
        return a string that contains information about all pizzas ordered
        
        :return: string
       
        """
        
        s = ""
        for piz in self.pizzas:            
            s += (f"Crust: {piz.crust}, Sauce: {piz.sauce}, Cheese: {piz.cheese}, Toppings: {piz.toppings}, Cost: {piz.price}\n")
        s += (f"Total Cost: {self.total_cost}")            
        return s
    
    #=================================
    # Set Order as paid once payment has been collected
    def order_paid(self)->bool:
        """
        Set the order as paid
        
        :return: Bool
       
        """

        self.paid = True
        return self.paid
    


   
        
        

