from collections import defaultdict

class Customer:
    def __init__(self,name,age,mobile_number,location,user_name):
        self.name=name
        self.age=age
        self.mobile_number=mobile_number
        self.location=location
        self.user_name=user_name

class Customer_Credentials:
    def __init__(self):
        self.credentials={}

    def Check_validity(self,user_name,password):
        if user_name in self.credentials and self.credentials[user_name]==password:
            return True
        return False
    
    def Verify_user_name(self,user_name):
        if user_name in self.credentials:
            return True
        return False
    


class Bank:
    
    def __init__(self):
        self.bank_customers=[]
        self.bank_transactions=defaultdict(list)
        self.bank_account_number=1001
    
    def Create_account(self,customer_details):
        customer_details.bank_account_number=int(self.bank_account_number)
        customer_details.bank_balance=int(0)
        self.bank_customers.append(customer_details)
        self.bank_account_number+=1
        if customer_details.bank_account_number not in self.bank_transactions:
            self.bank_transactions[customer_details.bank_account_number].append("ACCOUNT HAS BEEN CREATED SUCCESSFULLY")

        print("YOUR BANK ACCOUNT HAS BEEN CREATED SUCCESSFULLY")
        print("=====YOUR BANK ACCOUNT DETAILS=====")
        print("-----YOUR FULL NAME-------- : ",customer_details.name)
        print("-----YOUR AGE --------------: ",customer_details.age)
        print("-----YOUR MOBILE NUMBER-----: ",customer_details.mobile_number)
        print("-----YOUR ADDRESS---------- : ",customer_details.location)
        print("-----YOUR ACCOUNT NUMBER--- : ",customer_details.bank_account_number)
        print("-----YOUR BANK BALANCE----- : ",customer_details.bank_balance)
        print("-----YOUR USER NAME-------- : ",customer_details.user_name)

        print("----------DO NOT FORGET OR LOOSE YOUR LOG-IN CREDENTIALS , IT IS MANDATORY FOR YOUR ACCESS INTO ACCOUNT----------")
    

    def Check_bank_balance(self,account_number):
        balance_condition=False
        for customer in self.bank_customers:
            if customer.bank_account_number == account_number:
                print("YOUR CURRRENT BANK BALANCE IS :" ,customer.bank_balance)
                balance_condition=True
                break
        if not balance_condition:
            print("INVALID BANK ACCOUNT NUMBER")
    
    def Deposit_amount(self,account_number,amount):
        deposit_condition=False
        for customer in self.bank_customers:
            if customer.bank_account_number == account_number:
                customer.bank_balance+=amount
                self.bank_transactions[customer.bank_account_number].append(str(amount)+" RUPEES HAS BEEN DEPOSITED INTO YOUR ACCOUNT")
                print("AMOUNT HAS BEEN DEPOSITED SUCCESSFULLY , PLEASE CHECK YOUR BANK BALANCE")
                print("YOUR CURRENT BANK BALANCE IS : ",customer.bank_balance)
                deposit_condition=True
                break

        if not deposit_condition:   
            print("INVALID ACCOUNT NUMBER , PLEASE ENTER VALID ACCOUNT NUMBER")

    
    def With_Draw_Cash(self,account_number,amount_need):
        withdrawl_condition=False
        
        for customer in self.bank_customers:
            if customer.bank_account_number == account_number:
                if customer.bank_balance>=amount_need:
                    customer.bank_balance-=amount_need
                    self.bank_transactions[customer.bank_account_number].append(str(amount_need)+" RUPEES HAS BEEN WITHDRAWL FROM YOUR ACCOUNT")
                    print("AMOUNT HAS BEEN WITH-DRAWL SUCCESSFULLY ")
                    print("YOUR CURRENT BANK BALANCE IS  " , customer.bank_balance)
                elif customer.bank_balance<amount_need:
                    print("YOU DO NOT HAVE THE REQUIRED FUNDS IN YOUR BANK ACCOUNT")
                withdrawl_condition=True
                break

        if not withdrawl_condition:
            print("INVALID ACCOUNT NUMBER , PLEASE ENTER VALID ACCOUNT NUMBER")

    

    def Transfer_money(self,sender_account_number,receiver_account_number,transfer_money):
        first_person=0
        second_person=0
        for customer in self.bank_customers:
            if customer.bank_account_number==sender_account_number:
                first_person+=1
                if customer.bank_balance>=transfer_money:
                    first_person+=1
            
            if customer.bank_account_number==receiver_account_number:
                second_person+=1
        
        if first_person ==0:
            print("PLEASE ENTER YOUR ACCOUNT NUMBER CORRECTLY")
        
        elif second_person==0:
            print("INVALID ACCOUNT NUMBER,PLEASE CHECK THE ACCOUNT NUMBER YOU HAVE ENTERED FOR THE TRANSATION")
        
        elif first_person==1:
            print("YOU HAVE INSUFFICIENT FUNDS TO TRANSFER THE AMOUNT")
        
        else:
            for customer in self.bank_customers:
                if customer.bank_account_number==sender_account_number:
                    customer.bank_balance-=transfer_money
                    self.bank_transactions[customer.bank_account_number].append(str(transfer_money)+" RUPEES HAS BEEN DEBITED FROM YOUR ACCOUNT " )

                if customer.bank_account_number==receiver_account_number:
                    customer.bank_balance+=transfer_money
                    self.bank_transactions[customer.bank_account_number].append(str(transfer_money)+" RUPEES HAS BEEN CREDITED INTO YOUR ACCOUNT")
            
            print("MONEY HAS BEEN TRANSFERED SUCCESSFULLY .")
    
    def Mini_statement(self,account_number):
        if account_number not in self.bank_transactions:
            print("INVALID ACCOUNT NUMBER HAVE BEEN ENTERED ! , PLEASE RE-VERIFY YOUR ACCOUNT NUMBER")
        else:
            last=4
            total=len(self.bank_transactions[account_number])-1
            transactions=min(total,last)
            while transactions>=0:
                print(self.bank_transactions[account_number][transactions])
                transactions-=1
        

    
    def Display_all_customers(self):

        print("CUSTOMER_NAME-----CUSTOMER_AGE-----CUSTOMER_PHONE_NUMBER-----BANK-ACCOUNT_NUMBER")
        for customer in self.bank_customers:
            print(customer.name,"---",customer.age,"---",customer.mobile_number,"---",customer.bank_account_number)

    


def main():
    bank=Bank()
    secret_data=Customer_Credentials()

    while True:
        print("""
        ====== WELCOME TO NATIONAL BANK =======
        PLEASE ENTER YOUR CHOICE
              
        1. CREATE A BANK ACCOUNT
        2. CHECK BANK BALANCE
        3. TRANSFER AMOUNT
        4. WITH-DRAW AMOUNT
        5. DEPOSIT AMOUNT
        6. MINI STATEMENT 
        7. EXIT
        8. DISPLAY ALL CUSTOMERS OF BANK

        """)
        
        choice = input("Enter Your Choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            customer_name=input("PLEASE ENTER YOUR FULL NAME : ")
            customer_age=int(input("PLEASE ENTER YOUR AGE : "))
            customer_mobile_number=int(input("PLEASE ENTER YOUR MOBILE NUMBER : "))
            customer_location=input("PLEASE ENTER YOUR CITY : ")
            customer_user_name=input("PLEASE ENTER YOUR PREFFERED USER-NAME : ")
            customer_password=input("PLEASE ENTER YOUR PREFFERED PASSWORD : ")
            customer_password_match=input("RE-ENTER YOUR PASSWORD : ")

            if customer_password!=customer_password_match:
                print("PASSWORDS DOESNT MATCH , PLEASE TRY AGAIN !")
            
            elif secret_data.Verify_user_name(customer_user_name):
                print("PLEASE ENTER ALTERNATE USER NAME , USER NAME ALREADY EXISTS !")
            
            else:
                customer_details = Customer(customer_name,customer_age,customer_mobile_number,customer_location,customer_user_name)
                secret_data.credentials[customer_user_name]=customer_password
                bank.Create_account(customer_details)
        
        elif choice == 2:
            customer_user_name=input("PLEASE ENTER REGISTERED USER-NAME : ")
            customer_password=input("PLEASE ENTER PASSWORD : ")
            if secret_data.Check_validity(customer_user_name,customer_password):
                customer_bank_account_number = int(input("PLEASE ENTER YOUR BANK ACCOUNT NUMBER : "))
                bank.Check_bank_balance(customer_bank_account_number)
            else:
                print("INVALID LOGIN CREDENTIALS , PLEASE VERIFY YOUR CREDENTIALS BEFORE LOGGING IN !")

        elif choice == 3:
            customer_user_name=input("PLEASE ENTER REGISTERED USER-NAME : ")
            customer_password=input("PLEASE ENTER PASSWORD : ")
            if secret_data.Check_validity(customer_user_name,customer_password):
                sender_bank_account_number = int(input("PLEASE ENTER YOUR BANK ACCOUNT NUMBER : "))
                receiver_bank_account_number = int(input("PLEASE ENTER RECEIVER BANK ACCOUNT NUMBER : "))
                amount_transfer = int(input("ENTER THE AMOUNT NEEDED TO BE TRANSFERED : "))
                bank.Transfer_money(sender_bank_account_number,receiver_bank_account_number,amount_transfer)
            else:
                print("INVALID LOGIN CREDENTIALS , PLEASE VERIFY YOUR CREDENTIALS BEFORE LOGGING IN !")

        elif choice == 4:
            customer_user_name=input("PLEASE ENTER REGISTERED USER-NAME : ")
            customer_password=input("PLEASE ENTER PASSWORD : ")
            if secret_data.Check_validity(customer_user_name,customer_password):
                customer_bank_account_number = int(input("PLEASE ENTER YOUR BANK ACCOUNT NUMBER : "))
                amount = int(input("ENTER THE AMOUNT NEEDED TO BE WITHDRAWL : "))
                bank.With_Draw_Cash(customer_bank_account_number, amount)
            else:
                print("INVALID LOGIN CREDENTIALS , PLEASE VERIFY YOUR CREDENTIALS BEFORE LOGGING IN !")
             
        elif choice == 5:
            customer_user_name=input("PLEASE ENTER REGISTERED USER-NAME : ")
            customer_password=input("PLEASE ENTER PASSWORD : ")
            if secret_data.Check_validity(customer_user_name,customer_password):
                customer_bank_account_number = int(input("PLEASE ENTER YOUR BANK ACCOUNT NUMBER : "))
                amount = int(input("ENTER THE AMOUNT NEEDED TO BE DEPOSIT : "))
                bank.Deposit_amount(customer_bank_account_number, amount)
            else:
                print("INVALID LOGIN CREDENTIALS , PLEASE VERIFY YOUR CREDENTIALS BEFORE LOGGING IN !")
            
        elif choice == 6:
            customer_user_name=input("PLEASE ENTER REGISTERED USER-NAME : ")
            customer_password=input("PLEASE ENTER PASSWORD : ")
            if secret_data.Check_validity(customer_user_name,customer_password):
                customer_bank_account_number = int(input("PLEASE ENTER YOUR BANK ACCOUNT NUMBER : "))
                bank.Mini_statement(customer_bank_account_number)
            else:
                print("INVALID LOGIN CREDENTIALS , PLEASE VERIFY YOUR CREDENTIALS BEFORE LOGGING IN !")
        elif choice == 7:
            break
        else:
            print("Invalid input. Please enter number between 1-7 ")        
    print("Thank you for banking with us :)")


if __name__=="__main__":
    main()



                

        

    