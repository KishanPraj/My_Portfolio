class Person:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
class Customer(Person):
    def __init__(self, first_name, last_name, acc_num, bal=0):
        super().__init__(first_name, last_name)
        self.acc_num=acc_num
        self.bal=bal
    def __str__(self):
        return f"Client: {self.first_name} {self.last_name}\nAccount Balance {self.acc_num}: ${self.bal}"
    def deposit(self, a_deposit):
        self.bal+=a_deposit
        print("Deposit Recieved")
    def withdraw(self,a_withdraw):
        if self.bal>=a_withdraw:
            self.bal-=a_withdraw
            print("Success")
        else:
            print("Not enough cash")
def create_client():
    firstnamect=input('Enter First Name:')
    lastnamect=input('Enter Last Name:')
    account_number=input("Enter Account Number: ")
    client1=Customer(firstnamect, lastnamect, account_number)
    return client1
def start():
    my_customer=create_client()
    print(my_customer)
    opt=0
    while opt!="E":
        print("Choose: Deposit (D), Withdraw (W), or Exit (E)")
        opt=input()
        if opt=="D":
            dep_amount=int(input("Deposit Amount: "))
            my_customer.deposit(dep_amount)
        elif opt=="W":
            with_amount=int(input("Withdraw Amount: "))
            my_customer.withdraw(with_amount)
        print(my_customer)
    print("Thank you for using Kishan's Amazing Bank!")
start()
