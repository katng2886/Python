'''This is the class file for Instant Cart application: '''

class SmartCart(dict):
    '''dict subclass to maintain user cart'''
    discount_coupon = {'SAVE10': 10, 'SAVE20': 20, 'SAVE30': 30}
    
    def subtotal(self):
        '''Returns subtotal from a dictionary object'''
        '''Calculate the subtotal for the instant cart. This is the price before tax'''
        total = 0
        for item, quantity in self.items():
            total += float(item.get_price()) * quantity
        return round(total,2) 
        #iterate over each key, value in dict
        #obtain the price and quantity for each key
        #add to total variable after multiplying price with the quantity
    def tax(self): 
        '''Calculate price with tax.
        Virginia's tax for grocery product: 1%'''
        tax = round(0.01 * self.subtotal(),2)
        return tax
    def total(self): # before discount
        '''Calcutlate the total price with NO DISCOUNT'''
        subtotal = self.tax() + self.subtotal() #tax + total
        return round(subtotal,2)
    def discount(self, discount_cp): #calculate discount
        '''When the customer have discount -> apply discount'''
        discount_value = self.discount_coupon.get(discount_cp, 0) #look for the discount key in the discount_coupon dict -> if no matching -> return 0.
        return int(discount_value) #return discount value. Ex: 10%, 20%, 30%
    def discounted_total(self, discount_cp): #after discount if applied
        '''Calculate the price with the tax and discount applied'''
        discounted_total = self.total() - self.discount(discount_cp) * self.total()*0.01
        return f"${round(discounted_total,2)}"
        
class Item(object):
    '''Item class defines an item
    available in store. Item object saved in
    lists per category'''
    items= []
    def __init__(self, name, category, price, expiration_date):
        '''Initialization method'''
        #assuming all the variables are private.
        self.__name = name 
        self.__category = category
        self.__price = price
        self.__expiration_date = expiration_date
        Item.items.append(self)
    #define all the get methods to obtain the instance variables. 
    def get_category(self): 
        return self.__category
    def get_name(self): 
        return self.__name
    def get_price(self): 
        return self.__price
    def get_expiration_date(self): 
        return self.__expiration_date
    #define a __str__ method to obtain all four instance attributes.        
    def __str__(self): 
        return f"Category: {self.__category}\nName: {self.__name}\nPrice: {self.__price}\nExpiration date: {self.__expiration_date}"
    
class Dairy(Item): #Dairy
    dairy_items = []
    def __init__(self, name, speciality, category, price, expiration_date):
        super().__init__(name, category, price, expiration_date)
        self.__speciality = speciality
        Dairy.dairy_items.append(self)

    def get_spec(self):
        #return the specialty
        return self.__speciality

class FruitVegetable(Item): #sublcass of Item
    veg_fruit_items = []
    def __init__(self, name, speciality, category, price, expiration_date):
        super().__init__(name, category, price, expiration_date)
        self.__speciality = speciality
        FruitVegetable.veg_fruit_items.append(self)
        
    def get_spec(self): 
        return self.__speciality
        

class Seafood(Item): 
    seafood_items = []
    def __init__(self, name, speciality, category, price, expiration_date):
        super().__init__(name, category, price, expiration_date)
        self.__speciality = speciality
        Seafood.seafood_items.append(self)
    def get_spec(self): 
        return self.__speciality
        
class Poultry(Item): 
    poultry_items = []
    def __init__(self, name, speciality, category, price, expiration_date):
        super().__init__(name,category ,price, expiration_date)
        self.__speciality = speciality
        Poultry.poultry_items.append(self)
    def get_spec(self): 
        return self.__speciality
    
#define FruitVegetable, Seafood and Poultry Subclass
#these are alll polymorphic class. 

#process file
#open file, read information, create different category of objects
with open('Instant Cart/grocery.txt') as f: #open the local file text database
    for line in f:
        item = line.strip('').split('|') #Reading from the text file.
        if 'Fruit' in line or 'Vegetable' in line: #Sort by category
            if len(item) == 5:
                if 'OR' in line:
                    name, speciality, category, price, expiration_date = item
                    speciality = 'Organic'
                    cart = FruitVegetable(name, speciality, category, price, expiration_date)
            else:
                name, category, price, expiration_date = item
                cart = FruitVegetable(name, 'Non-organic', category, price, expiration_date)
        elif 'Dairy' in line:  
            if len(item) >= 5:
                if 'PR' in line: 
                    name, speciality, category, price, expiration_date = item
                    speciality = 'Pasture Raised'
                    cart = Dairy(name, speciality, category, price, expiration_date)
            else:
                name, category, price, expiration_date = item
                cart = Dairy(name, 'No Pasture Raised', category, price, expiration_date)
        elif 'Seafood' in line: 
            if len(item) >= 5:
                if 'WC' in line: 
                    name, speciality, category, price, expiration_date = item
                    speciality = 'Wild Caught'
                    cart = Seafood(name, speciality, category, price, expiration_date)
            else:
                name, category, price, expiration_date = item
                cart = Seafood(name, 'Farm Raised', category, price, expiration_date)
        elif 'Poultry' in line: 
            if len(item) >= 5:
                if 'OR' in line:
                    name, speciality, category, price, expiration_date = item
                    speciality = 'Organic'
                    cart = Poultry(name, speciality, category, price, expiration_date)
            else:
                name, category, price, expiration_date = item
                cart = Poultry(name, 'Non-Organic', category, price, expiration_date)
        else: 
            print('Invalid option')
        
