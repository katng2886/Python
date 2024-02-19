
#define Task class

class Task(object):
    all_tasks = []
    #your code here
    #define init, set, get and str methods.
    def __init__ (self, description, priority, status ): 
        self.description = description
        self.priority = priority
        self.status = status
        Task.all_tasks.append(self)
    
    def get_description(self):
        return f"\nThe task's description is: {self.description}\n"
    def get_priority(self):
        return f"\nThe task's priority is: {self.priority}\n"
    def get_status(self):
        return f"\nThe task's priority is: {self.status}\n"
    def set_description(self, new_description): 
            self.description = new_description
            return f"\nNew description: {new_description}\n"
    def set_priority(self, new_priority): 
            self.priority = new_priority
            return f"\nNew priority: {new_priority}\n"
    def set_status(self, new_status): 
        self.status = new_status
        return f"\nNew status: {new_status}\n"
    def __str__(self):
         return '{}-{}-{}'.format(self.description, self.priority, self.status)
    


def main():
    with open('HA1.txt') as f:
        for line in f: 
            description, priority, status = line.strip('\n').split(',')
            t = Task(description, priority, status)
            
        #get the information from file and
        #create Task objects.
        
    #user menu
    menu = '[get] display\n[set] modify '
    while True:
        print('************* Current Tasks ***************\n')
        for task in Task.all_tasks: #task is Task object from all_tasks list
            print(task) #print a Task object 
        print('*************')

        print(menu)
        option = input('Type an option or type "e" to exit: ') #ask user to type option
        
       
        if option == 'get':
            ask_description = input("Enter task's description: ")
            ask_different_option = input("Enter options (d,p,s): ")
            for i in Task.all_tasks:
                if ask_description == i.description: #loop through all_tasks list and find if it matches the input description
                    if ask_different_option =='d': #if it matches -> print description
                        print(i.get_description())
                    elif ask_different_option == 'p': 
                        print(i.get_priority()) 
                    elif ask_different_option == 's': 
                        print(i.get_status())
        elif option == 'set': 
            ask_description = input("Enter task's description: ")
            for i in Task.all_tasks:
                if ask_description == i.description:
                    ask_different_option = input("Enter options (d,p,s): ")
                    if ask_different_option =='d':
                        new_description  = input('Enter new description: ')
                        print(i.set_description(new_description))
                    elif ask_different_option == 'p':
                        new_priority = input('Enter new priority: ')
                        print(i.set_priority(new_priority))
                    elif ask_different_option == 's':
                        new_status = input('Enter new status: ')
                        print(i.set_status(new_status))
        elif option == 'e': 
            print('Good bye!')
            f = open('HA1.txt', 'w')
            for item in Task.all_tasks: 
                f.write(f"{item.description},{item.priority},{item.status}\n")
            exit(0)

                    

            #ask for user description of the task to display
            #ask for different options (d/p/s) to display
            #use a for loop to go over all_tasks list - see above
            #and then use the loop var. task to call method get_description
            #to see which  one matches with the user description
            #display the information according to d, p or s
            
            
#call main   
main()
