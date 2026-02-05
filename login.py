class Business:
    def __init__(self, name, category, balance = 0):
        self.name = name
        self.category =category
        self.balance = balance
        self.is_open = False
        self.loging_attempts = 0

    def describe_shop(self):
        print(f"Welcome to {self.name}, we are {self.category}")
        print(f"we currently have {self.balance} in the bank")

    def make_sale(self, amount):
        self.balance += amount
        print(f"nayan! just made ${amount} New_Balance: {self.balance}")

    def open_store(self):
        self.is_open = True
        print(f"{self.name} Is now open For The customers! ")
    def increment_login_attempts(self):
        self.loging_attempts += 1
        print('Login Attempt recored: ')

    def reset_login_password(self):
        '''reseting Loging Password To Zero'''
        self.loging_attempts = 0
        

shop = Business("Glaxy Gameing", "Video Game Store", 0)
print("-"*10)

shop.describe_shop()
shop.open_store()
shop.make_sale(10000)

shop.increment_login_attempts()
shop.increment_login_attempts()
shop.increment_login_attempts()
shop.increment_login_attempts()

print(f'Attmepts So far {shop.loging_attempts}')

shop.reset_login_password()
print('Rest The Login Attempts To = 0')
print("="*50)