# python bank program
# created a virtual environment and ran this code = python -m venv bankProgram
#to activate the virtual environment = bankProgram\scripts\activate.bat
# here function should return something(in our case number) cause we are adding a function with a numeric data type.
# other wise if there is no return type then the function return none itself and when we add to other data type it will return type error

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
    print("-----------------------")

def deposit():
    amount=float(input("Enter a amount to be deposited:-"))
    if amount<0: # when the code tries to add none(which happens when there is no return type)to a balance(which is at choice 2) it will create type error    
        print("This is not a valid deposit")
        print("-----------------------")
        return 0# having return 0 here prevents from adding invalid amount to balance and always adds 0 if invalid 
        # if there is no  return statement and when we add this function to something its going to return none
    else:
        print(f"${amount} has been deposited successfully!!!")
        print("-----------------------")
        return amount
        

def withdraw(balance):
    amount=float(input("Enter the amount to be withdraw:-"))
    if amount<0:
        print("This is not a valid withrawl")
        print("-----------------------")
        return 0 
    if amount>balance:
        print("Insufficient fund!!!!!")
        print("-----------------------")
        return 0 
    else:
        print(f" The amount you are withdrawing is ${amount} and is successfullly withrawl!!!")
        print("-----------------------")
        return amount

def main():

    balance=0 # since it is defined outside and is a global variable it can be accessed when we use other options and keeps on chaning until we terminate the program
    is_running=True

    while is_running:
        print("BANKING PROGRAM")
        print("1.SHOW")
        print("2.DEPOSIT")
        print("3.WITHDRAW")
        print('4.EXIT')
        print("-----------------------")

        choice=input("Enter your choice among these four options:-")

        if choice=='1':
            show_balance(balance)

        elif choice=='2':
            balance+=deposit(balance)
            
        
        elif choice=='3':
            balance-=withdraw(balance)
        
        elif choice=='4':
            is_running=False

        else:
            print("that is not a valid choice")
            print("-----------------")

    print("Thank you have a nice day")

if __name__=="__main__": # this means that this program can be imported or run standalone.
    main()