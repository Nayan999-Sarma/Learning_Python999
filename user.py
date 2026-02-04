class User:
    #initilize th eattributes
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        #Gives All the information about The User
    def describe_user(self):
        print('---Person Information----')
        print(f'Person Name {self.first_name} {self.last_name}')
        print(f'Person Age {self.age}')
        print(f'Person city {self.city}')
        #Friendly greeting to friends
    def greet_user(self):
        print('--Greeting to The User---')
        print(f'Hi {self.first_name} {self.last_name} How are you! ')

user = User('Nayan', 'Sarma', 22, 'Guwahati')
user.describe_user()
user.greet_user()
print('---New User----')
#Creating instance people
user1 = User('Guarav', 'Yadav', 24, 'Kolkata')
user2 = User('Appu', 'Kalita', 22, 'Guwahati')
user3 = User('Dipankar', 'Chutiya', 24, 'Guwahati')

user1.describe_user()
user1.greet_user()
print('-'*10) 
print()
user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()


