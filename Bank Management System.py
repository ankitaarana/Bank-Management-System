accounts={101:{'name':'Ram',"Balance":700,"PIN":1234},
          102:{'name':'Ankita',"Balance":1500,"PIN":4321}, 
          103:{'name':'Shyam',"Balance":3000,"PIN":4567}} 
def home_page():
    print("Press '1' for Existing user: ")
    print("Press'2' for New User: ")
    Choice=int(input("Enter your choice(1-2): "))
    if (Choice==1):                          #existing user
        existing_user()
    elif(Choice==2):                         #new user
        new_user()



def existing_user():
    account_number = int(input("Enter your account number: "))
    pin=int(input("Enter PIN: "))

    if account_number in accounts and accounts[account_number]["PIN"]==pin:
        print("\n Login successful,Welcome!",accounts[account_number]["name"])
        main_menu(account_number)
    else:
            print("Invalid input. Please check your details and try again")
            existing_user()
    
def new_user():
    import random
    print("Welcome to ABC Bank")
    name=input("Enter your name:  ")
    account_number =random.randint(10000,20000)
    pin=input("Create your 4 digit PIN: ")
    accounts[account_number]={"name":name,"PIN": pin, "Balance":0}  #start with zero balance#
    print("Successfully created your account, please Login to Home Page ")
    print("Account Number: ",account_number)
    print("name: ",name)
    print("PIN: ",pin)
    calling()
                
def calling():
    print("\n Press '1' for Main page")
    print("Press'2' for Home page")
    value=int(input("Enter your input(1-2): "))
    if value==1:
        main_menu()
    elif value==2:
        home_page()    

def main_menu(account_number):                    #Main Menu==============================================================
    print("\n Press '1' for Credit amount")
    print("Press '2' for Debit amount")
    print("Press '3' to Check Balance")
    print("Press '4' to Delete Account")
    print("Press '5' for Home page")
    choice=int(input("Enter your choice (1-5): "))
    if choice==1:                     # to credit amount in account=========================================
        amount=float(input("Enter credit amount"))
        accounts[account_number]["Balance"]= accounts[account_number]["Balance"] +amount
        print("Successfully credited",amount,"on your account. New Balance", accounts[account_number]["Balance"])
        calling()

    elif choice==2:                   # to debit the amount from account======================================
        debit=float(input("Enter amount to be Debited: "))
        if debit<=accounts[account_number]["Balance"]:
            accounts[account_number]["Balance"]= accounts[account_number]["Balance"] -debit
            print("Successfully debited",debit,"from your account. Remaining Balance", accounts[account_number]["Balance"])
        else:
            print("Oops,There is insufficient balance in your account")
        calling()

    elif choice==3:                   # to check user's balance
        Balance=accounts[account_number]["Balance"]
        print("Your current Balance is ", Balance)
        calling()

    elif choice==4:                    # to delete users' account permanantely
        account_number=int(input("Please confirm your account number: "))
        if account_number in accounts:
            confirm =input("Are you sure you want to delete your account?(Yes/No): ")
            if confirm.lower() =="yes":
                print("Your account has been deleted")
                del accounts[account_number]
                calling()
            elif confirm.lower() =="no":
                print("Process aborted")
                calling()
        else:
             print("No account found. Please try again")
             calling()

#main program

home_page()




# a={"101":{"name":"sheetal","balance":1000,"PIN":123}}
# for i in a :
#     print(a[i])
#     for j in a[i]:
#         print(j,a[i][j])