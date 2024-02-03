statetotal = 0.04
countytaxrate = 0.02

def main(): #that calls your other function
    print("Welcome to the total tax calculator program!")
    monthly_sales = inputData()
    printData(monthly_sales)

def inputData(): #that will ask for the monthly rate
    return int(input("Enter your monthly sales: $"))

def calCounty(monthly_sale): #that will calculate the county tax
    return monthly_sale * countytaxrate

def calState(monthly_sale): #that will calculate the tax rate
    return monthly_sale * statetotal

def calcTotal(countytaxrate, statetotal, monthly_sale):
    return (countytaxrate + statetotal) * monthly_sale
def printData(monthly_sales): #that will display the county tax, the state tax and the total tax
    county_tax = calCounty(monthly_sales)
    state_tax = calState(monthly_sales)
    total_tax = calcTotal(countytaxrate,statetotal, monthly_sales)

    print(f'The county tax is: $ {county_tax: .2f}')
    print(f'The state tax is: $ {state_tax: .2f}')
    print(f'The total tax is: $ {total_tax: .2f}')

main()

