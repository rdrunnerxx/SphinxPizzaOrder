#Name: Mehdi (MED) Shakeri(mshakeri4@jh.edu)

#Module Info: Module 4 - Pytest and Sphinx, due 06/30/2024 at 11:59pm 



# Our pizza inventory items
Crust   = [ ("Thin", 5),        ("Thick", 6),       ("Gluten_Free", 8)]
Sauce   = [ ("Marinara", 2),    ("Pesto", 3),       ("Liv_Sauce", 5)]
Toppings= [ ("Pineapple", 1),   ("Pepperoni", 2),   ("Mushrooms", 3)]
Cheese  = [ ("None", 0),        ("Mozzarella", 0)]                          # with/without cheese is free

#Pizza objects and associated costs
class Pizza:
    
    # Initialize a pizza, variables and cost
    def __init__(self, crust, sauce, cheese, toppings):                     # sauce and toppings are list 
        self.price = 0                                                      # initizalize price to 0
        self.create_pizza(crust, sauce, cheese, toppings)    
   
    #==================================    
    #Determine cost of the pizza
    def cost(self)->float:
        self.price  = self.crustprice + self.sauceprice + self.toppingsprice            
        return self.price
    
    
    #=================================
    # Input the customers order for a given pizza
    # Initialize the pizza object and attach to the order
    # Update the cost and returns cost
    def create_pizza(self, crust, sauce, cheese, toppings)->float:
        self.crustprice = 0
        for i in range(len(Crust)):                
            if (crust == Crust[i][0]):
                self.crust      = Crust[i][0]
                self.crustprice = Crust[i][1]
                break                                          # only one item in crust
            
        self.sauce = []                                        # a list, sauce can have multiple items
        self.sauceprice = 0
        for sa in sauce:
            for i in range(len(Sauce)):                
                if (sa == Sauce[i][0]):
                    self.sauce.append( Sauce[i][0])
                    self.sauceprice +=  Sauce[i][1]
                
        self.cheeseprice = 0
        for i in range(len(Cheese)):                
            if (cheese == Cheese[i][0]):
                self.cheese = Cheese[i][0]
                break                                          # only one item in cheese, price is same (0)
                
        self.toppings = []                                     # a list, topping can have multiple items
        self.toppingsprice = 0
        for top in toppings:
            for i in range(len(Toppings)):                
                if (top == Toppings[i][0]):
                    self.toppings.append(Toppings[i][0])
                    self.toppingsprice += Toppings[i][1]
        
        return self.cost()                                    # updates cost using selected items and returns price

    #=================================
    # Print a pizza and cost
    def __str__(self):
        return(f"Crust: {self.crust}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {self.toppings}, Cost: {self.price}")
    
             
        
#=======================
# For Testing 
# if __name__ == "__main__":
   
#     #create a new pizza
#     my_pizza = Pizza("Thin", ["Pesto"], "Mozzarella", ["Mushrooms"])
#     print(str(my_pizza))
    
#     my_pizza = Pizza("Thick", ["Marinara"], "Mozzarella", ["Mushrooms"])
#     print(str(my_pizza))

#     my_pizza = Pizza("Gluten_Free", ["Marinara"], "Mozzarella", ["Pineapple"])
#     print(str(my_pizza))

#     my_pizza = Pizza("Thin", ["Liv_Sauce", "Pesto"], "Mozzarella", ["Mushrooms", "Pepperoni"])
#     print(str(my_pizza))
    

    


