# import tkinter
from tkinter import *
#import class from class file
from Instant_Cart_file import Item, FruitVegetable, Seafood, Dairy, Poultry, SmartCart
#import GUI Module
from functools import partial
import random, string #used in random receipt no function

class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) #Frame class initialization
        self.init_container() #initialize all widget containers
        self.cart = SmartCart() #initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.welcome() #start the application
        self.data = StringVar(self, 'Subtotal: 0.0') #Associated with subtotal label

        
    def init_container(self):
        '''Initialize widget containers'''
        self.quantity_entries = [] #qunatity entry list
        self.states = [] #holds state if selected/not i-th list item holds selection for i-th item

    def clear_frame(self): 
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()


    def welcome(self):
        '''1. Welcome window - refer spec file for details'''
        self.clear_frame()
        Label(self, text = '****Welcome to Instant Cart!****', background="gray70").pack(side = TOP)
        #your code here
        #Start Ordering: Button – start the program, command = shop_by_category
        #Exit Application: Button – exit the program, command = exit_application
        start_bt = Button(self, text = 'Start ordering', command= self.shop_by_category)
        exit_bt = Button(self, text= 'Exit Application', command= self.exit_application)
        #create layout
        start_bt.pack()
        exit_bt.pack()
        
    def shop_by_category(self):
        '''2. Widget to display different category of items - refer spec file for details'''
        self.clear_frame()
        self.init_container()
        #your code here
        #a.	Choose Category: label 
        category_lbl = Label(self, text='Choose Category')
        category_lbl.grid(row=0, column=0)
        #b.	Dairy: Button – command = start (code below)
        #partial is a special method to pass an argument during button command
        #for dairy category Dairy.dairy_items will be passed to display all dairy item
        self.dairy_button  = Button(self, text = "Dairy", command=partial(self.start, Dairy.dairy_items))
        #your code here
        
        
        #Create VegetableAndFruit button
        #c.	Vegetable and Fruit - veg_fruit_button: Button – command = start (Same as dairy)
        self.vegetable_fruit = Button(self, text='Vegetable and Fruit', command=partial(self.start, FruitVegetable.veg_fruit_items))
        
        #Create Poultry and Meat button 
        #d.	Poultry and Meat - poultry_meat_button: Button – command = start(Same as dairy)
        self.poultry_button = Button(self, text='Poultry and Meat', command=partial(self.start, Poultry.poultry_items))
        
        #Create Seafood button 
        #e.	Seafood: Button - seafood_button – command = start(Same as dairy)
        self.seafood_button = Button(self, text='Seafood', command=partial(self.start, Seafood.seafood_items))
        
        #Create Go back button
        #f.	Go Back: Button – command = welcome (go back to #1)
        #layout manager for all the widgets
        go_back_button = Button(self, text='Go back', command=self.welcome)
        
        
        #create layout manager: dairy, vegetable and fruit, poultry and meat, seafood, go back
        self.dairy_button.grid(row=1, column=0)
        self.vegetable_fruit.grid(row=2,column=0)
        self.poultry_button.grid(row=3, column=0)
        self.seafood_button.grid(row=4, column=0)
        go_back_button.grid(row=5, column=0)
        
        
    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()
        
        #creating widgets for items using a for loop
        #iterative over each item of current items and
        #create that many checkbutton, price, exp date and specialty label,and quantity entry
        ######### or use enumerate
        for row, item in enumerate(current_items):
            self.states.append(IntVar()) #keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name(), variable=self.states[row])#create check buttons
            checkbutton.grid(row = row, column = 0)

            #your code here
            #create and layout a price label, set text to item.get_price()
            
            #create price_label
            price_label = Label(self, text= f"${item.get_price()}")
            price_label.grid(row=row, column=1)
            
            #create and layout a quantity entry and append to quantity_entries, set width = 2
            #create quantity entry 
            qty_entry = Entry(self, width=2)
            qty_entry.grid(row=row, column=2)
            self.quantity_entries.append(qty_entry)
            
            #create and layout exp_date_label and set text to item.get_expiration_date() method
    
            #create exp_date_label
            ex_date_label = Label(self, text= f"{item.get_expiration_date()}")
            ex_date_label.grid(row=row, column=3)
            
            #create and layout speciality_label and set text to item.get_spec() method
            speciality_label = Label(self, text =item.get_spec())
            speciality_label.grid(row=row, column=4)
            
        #create and layout subtotal label, set textvaribale = self.data so it changes
                
        sub_total_result_label = Label(self, textvariable=self.data)
        sub_total_result_label.grid(row=row+1, column=1)
        

        
        #with each add_to_cart button being pressedng
        #create and layout select categories: button, command = shop_by_category
        
        #Create and layout Select Categories button
        select_category_label = Button(self, text= 'Select Categories', command=self.shop_by_category )
        select_category_label.grid(row=row+2, column=0)
        #create and layout add_to_cart_button, command = partial(self.add_to_cart, current_items)
        
        #Create and layout add to cart button
        add_to_cart_bt = Button(self, text='Add to card', command=  partial(self.add_to_cart, current_items))
        add_to_cart_bt.grid(row=row+2, column=1)
        #create and layout button: checkout, command = self.checkout
        
        #Create and layout check out button
        check_out_bt = Button(self, text='Check Out', command=self.checkout)
        check_out_bt.grid(row=row+2, column=2)
        
    def add_to_cart(self, current_items): #####
        '''3. Added to cart, displays subtotal - see spec file for details layout'''
        for i in range(len(current_items)):
            #your code here
            #get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
            if (self.states[i].get() == 1): #check if items are selected
            #if item is selected:
                #get the product quantity from quantity_entries using get() function
                product_qty = int(self.quantity_entries[i].get())
                #obtain the product price
                product_price = float(current_items[i].get_price()) 
                #add item to self.cart dict where k = item object, v = quantity
                self.cart[current_items[i]] = product_qty #Item object = product_Qty
        #set the StringVar to be the current subtotal (SmartCart object self.cart has subtotal method)
        current_total =self.cart.subtotal()
        #refer to class file
        self.data.set(f'Subtotal: {current_total}')
        
    def get_receipt_number(self):
        '''Generate random receipt number'''
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()
        # your code here to create and layout following widgets:
        # refer to receipt frame
        self.get_receipt_number()
        # Your e-receipt: Label
        e_receipt_label = Label(self, text='Your E-receipt')
        e_receipt_label_start = Label(self, text= '**********')
        e_receipt_label.grid(row=0, column=0, columnspan=5)
        e_receipt_label_start.grid(row=1, column=0, columnspan=5)
        receipt_label = Label(self, text='Receipt Number: '+ self.get_receipt_number())
        receipt_label.grid(row=2, column=0, columnspan=2)
        # Receipt Number: Label - Randomly generated by program - text = get_receipt_number()
        # Name Price Quantity Expiration Date, Speciality: Header Label
        
        #create header label and its grids
        header_label1 = Label(self, text='Name: ')
        header_label1.grid(row=3, column=0)
        
        header_label2 = Label(self, text='Price: ')
        header_label2.grid(row=3, column=1)
        
        header_label3 = Label(self, text='Quantity: ')
        header_label3.grid(row=3, column=2)
        
        header_label4 = Label(self, text='Expiration Date: ')
        header_label4.grid(row=3, column=3)
        
        header_label5= Label(self, text='Speciality: ')
        header_label5.grid(row=3, column=4)
        # Item purchased, price quantity, exp.date, specialty: Label - from cart dictionary
        # using for loop to iterate over self.cart.items()
        
        #start the row = 4
        row =4
        for item, quantity in self.cart.items(): 
            print(item, quantity)
            name = Label(self, text=item.get_name())
            name.grid(row=row, column=0)
            
            price = Label(self, text=item.get_price())
            price.grid(row=row, column=1)
            
            quantity = Label(self, text= quantity)
            quantity.grid(row=row, column=2)
            
            exp_date = Label(self, text=item.get_expiration_date())
            exp_date.grid(row=row, column=3)
            
            speciality = Label(self, text= item.get_spec())
            speciality.grid(row=row, column=4)
            row = row+1
            
    # Subtotal: Label - get self.cart subtotal - new label 
        subtotal_label = Label(self, text= f'Before tax: ${round(self.cart.subtotal(),2)}')
        subtotal_label.grid(row=10, column=0, columnspan=5)
                
        # Tax: Label - 4.3%
        tax_label = Label(self, text=f'Tax: {self.cart.tax()}%')
        tax_label.grid(row=11, column=0, columnspan=5)
        # Total: Label - subtotal + tax
        
        #Create and layout Total after tax = subtotal + tax
        total_label = Label(self, text=f'Total after tax: ${self.cart.total()}') #call the total method from class file
        total_label.grid(row=12, column=0, columnspan=5)
        
        # Apply coupon label
        
        #Create and layout Apply coupon
        apply_coupon = Label(self, text='Apply coupon: ')
        apply_coupon.grid(row=13, column=0, columnspan=5)
        
        # An entry to obtain the discount code, for e.g. SAVE10
        
        #create and layout an Entry place to enter coupon code
        self.e_coupoun = Entry(self)
        self.e_coupoun.grid(row=14, column=0, columnspan=5)
        # Create discount calculate button and command is apply_discount
        
        #create Apply button, when clicked, display the coupon value
        discount_calculate = Button(self, text='Apply Discount', command=self.apply_discount)
        discount_calculate.grid(row=15, column=0, columnspan=5)
        
        # create two stringVar and initial text discount and discounted_total
        
        #Create and layout Discount label 
        self.discount = StringVar(self,'')
        self.discount_label_begin = Label(self, text = 'Discount:')
        self.discount_label_begin.grid(row=16, column=0, columnspan=4)
        self.discount_label = Label(self,textvariable= self.discount)
        self.discount_label.grid(row=16, column=1, columnspan=5)
        
        #create and layout Discounted Total label
        self.discounted_total = StringVar(self,'')
        self.discount_label_begin = Label(self, text='Discounted Total:')
        self.discount_label_begin.grid(row=17, column=0, columnspan=4)
        self.discounted_total_label = Label(self, textvariable= self.discounted_total)
        self.discounted_total_label.grid(row=17, column=1, columnspan=5)
        # ‘Thank you’ message: Label
        
        #Create and layout Thank you button
        thanks_label = Label(self, text='Thank You For Using InstantCart')
        thanks_label_start = Label(self, text='**********')
        thanks_label.grid(row=18, column=0, columnspan=5)
        thanks_label_start.grid(row=19, column=0, columnspan=5)
        # Exit application: Button – exit the program- command = exit_application
        
        #Create and layout Exit button -> when click -> Exit the application 
        exit_label = Button(self, text='Exit Application', command=self.exit_application)
        exit_label.grid(row=20, column=0, columnspan=5)
    def apply_discount(self):
        # your code here
        # check if user entered any discount
        # set the two stringVar to cart's methods discount and discounted_total
        discount_cp = self.e_coupoun.get()
        discount = self.cart.discount(discount_cp)
        #call the discount method
        self.discount.set(f"{discount}%")
        self.discounted_total.set(self.cart.discounted_total(discount_cp))

#main driver code
#your code here
#create root window
root = Tk()
root.title("Instant Cart") #set window title
#your code here
#create a myframe object and layout
#call mainloop
root.geometry("500x500")
f = MyFrame(root)
f.pack()
root.mainloop()
