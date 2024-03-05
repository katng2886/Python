#Creating an Program that display burger order and calculate the total amount as well as the tax

#define AddToCart class - a subclass of list class
class AddToCart(list): 
    def sub_total(self):
        total = 0
        for order in self: 
            total += order.get_price()
        return total
    def tax(self):
        #tax = 3.25%
        #tax =  self.sub_total()*0.025
        tax_total = self.sub_total() *0.0325
        sub_total = tax_total + self.sub_total()
        return f"Tax: {round(tax_total,2)}\nTotal: {round(sub_total,2)}"

        
#define SimpleBurger class
class SimpleBurger(object):
    cart = AddToCart() #class variable
    simple_burger_price = {'single': 7.99, 'double': 10.99} #class variable
    #Your Code Here
    def __init__(self, bun, patty): 
        self.bun = bun
        self.patty = patty
        SimpleBurger.cart.append(self)

    def get_price(self): 
        return SimpleBurger.simple_burger_price[self.patty]

    def __str__(self): 
        return '{}-{}'.format(self.bun, self.patty)

#define Subclasses
class CheeseBurger(SimpleBurger):
    cheese_type_price = {'american': 1.99, 'pepper jack': 0.99} #aditional price on base price
    #Your code here
    def __init__(self, bun, patty, cheese): 
        super().__init__(bun, patty)
        self.cheese = cheese
        
        #CheeseBurger.cart.append(self)

    def get_price(self):
        return CheeseBurger.cheese_type_price[self.cheese] + super().get_price()
    def __str__(self): 
        return '{}-{}-{}'.format(self.bun, self.patty, self.cheese)
    

#define VeggieBurger subclass
class Veggie(SimpleBurger):
    veggie_type = {'lettuce': 0.99, 'tomato': 0.99, 'caramelized onion': 2.99} #aditional price on base price
    #Your code here
    def __init__(self, bun, patty, veggie): 
        super().__init__(bun, patty, veggie)
        self.veggie = veggie
        Veggie.cart.append(self)

    def get_price(self):
        return Veggie.veggie_type[self.veggie] + super().get_price()
    
    def __str__(self): 
        return '{}-{}-{}'.format(self.bun, self.patty, self.veggie)
    

#-------------------------------- 
#main function/global code
#take user input on Burger type
#create object depending on type
choice = ''
print('******** Welcome to 209 Burger ******** \n\n')
while choice!='no':
    burger_type = input('\tEnter type of Burger(simple/cheese/veggie): ')
    bun = input('\tEnter bun type (white/wheat): ')
    patty = input('\tEnter patty type (single/double): ')
    if burger_type.lower() == 'simple': #create a SimpleBurger object
        order = SimpleBurger(bun, patty)
        print(f"Get price: ",order.get_price())
    
    elif burger_type.lower() == 'cheese':
        cheese = input('\tEnter cheese type (american/pepper jack): ')
        order = CheeseBurger(bun, patty, cheese)
        print(f"Get price: ", order.get_price())

    elif burger_type.lower() == 'veggie':
        veggie = input('\tEnter veggie type (letture/tomato/caramelized onion):')
        order = Veggie(bun, patty, veggie)
        print(F"Get price: ", order.get_price())           
    #your code here
    choice = input('Do you want to continue (yes/no): ')

#Print receipt
#calculate subtotal, tax and total.
print('\n\n\t******** Printing Receipt *******\n')
#follow the sample I/O
count = 0
for order in SimpleBurger.cart:
    print(count,"-", order, order.get_price())
    count+= 1
print("Subtotal:", SimpleBurger.cart.sub_total())
print(SimpleBurger.cart.tax())
     
print('\n\n\t******** Thank you for comming *******\n')