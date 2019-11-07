
# coding: utf-8

# In[1]:


from IPython.display import clear_output


class Account:
    def __init__(self, owner, check = 1000, save = 1000):
        self.owner = owner
        self.checking = check
        self.saving = save
    
    def deposit(self):
        account = input("Which Account Would You Like to Deposit In? Enter 'c' for Checking or 's' for Saving.")
        while account.lower() != 'c' and account.lower() != 's':
            account = input("Error! Please Enter 'c' for Checking or 's' for Saving.")
        amount = int(input("How Much Would You Like to Deposit?"))
        if account.lower() == 'c':
            self.checking += amount
            print("Deposited $" + str(amount) + " in Checking")
            print("You Now Have $" + str(amount) + " in Checking")
        else:
            self.saving += amount
            print("Deposited $" + str(amount) + " in Saving")
            print("You Now Have $" + str(amount) + " in Saving")
        clear_output()
        print(acc)
            
    def withdraw(self):
        max1 = 0
        account = input("Which Account Would You Like to Withdraw From? Enter 'c' for Checking or 's' for Saving.")
        while account.lower() != 'c' and account.lower() != 's':
            account = input("Error! Please Enter 'c' for Checking or 's' for Saving.")
        if account.lower() == 'c':
            max1 = self.checking
        else:
            max1 = self.saving
        amount = int(input("How Much Would You Like to Withdraw? You have $" + str(max1) + " Available."))
    
        while amount > max1:
            amount = int(input("Error! You Only Have $" + str(max1) + " Available!"))
        if account.lower() == 'c':
            print("Withdrew $" + str(amount) + " from Checking")
            self.checking -= amount
        else:
            self.saving -= amount
            print("Withdrew $" + str(amount) + " from Saving")
        clear_output()
        print(acc)
        
    def transfer(self):
        to = 1
        max1 = self.checking
        account = input("Which Account Would You Like to Transfer From? Enter 'c' for Checking or 's' for Saving.")
        while account.lower() != 'c' and account.lower() != 's':
            account = input("Error! Please Enter 'c' for Checking or 's' for Saving.")
        if account.lower() == 's':
            to = 2
            max1 = self.saving
        amount = int(input("How Much Would You Like to Transfer? You have $" + str(max1) + " Available."))
        while amount > max1:
            amount = int(input("Error! You Only Have $" + str(max1) + " Available!"))        
        if to == 1:
            self.checking -= amount
            self.saving += amount
        else:
            self.checking += amount
            self.saving -= amount
        clear_output()
        print(acc)
        
    def interest(self, rate, period, simple):
        self.rate = rate / 100
        if simple == True:
            self.original = self.saving
            self.saving += self.original * self.rate * period
            print("Simple Interest for " +  str(period) + " years")
            print("Your New Savings Balance is $" + str(self.saving))
        else:
            for x in range(0, period):
                self.saving = self.saving * (1 + self.rate)
            print("Compounded Interest for " + str(period) + " years")
            print("Your New Savings Balance is $" + str(self.saving))

            
    def __str__(self):
        return f"Owner: {self.owner} \nChecking: {self.checking} \nSaving: {self.saving}"


print('Welcome to GAO Bank!')
owner = input('May I Have Your Name?')
acc = Account(owner)
here = True
while here == True:
    clear_output()
    print(acc)
    option = int(input("Would You Like to: \n1. Withdraw \n2. Deposit \n3. Wait Years \n4. Transfer \n5. Exit\n"))
    if option == 2:
        acc.deposit()
    elif option == 1:
        acc.withdraw()
    elif option == 3:
        period = int(input("How Many Years do You Want to Wait? "))
        rate = int(input("What Rate Would the Interest Be?"))
        interest = input("Simple or Compound Interest? Please Choose 's' for Simple or 'c' for Compound")
        while interest.lower() != 's' and interest.lower() != 'c':
            interest = input("Error! Please Choose 's' for Simple or 'c' for Compound")
        if interest.lower() == 's':
            acc.interest(rate, period, True)
        else:
            acc.interest(rate, period, False)
    elif option == 4:
        acc.transfer()
    else:
        print('Bye!')
        break
    cont = input("Would You Like to Continue? 'y' for Yes or 'n' for No?")
    while cont.lower() != 'y' and cont.lower() != 'n':
        cont = input("Error! Please Select 'y' for Yes or 'n' for No.")
    if cont.lower() == 'n':
        here = False
        print('Bye!')    

