class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        #Get ready restaurant_name, cuisine_type
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        #Printing information
        print(f"{self.restaurant_name} serve {self.cuisine}")

    def open_restaurant(self):
        #printing that is open 
        print(f"{self.restaurant_name} is Open")
#First instance
print("----First Instance----")
restaurant = Restaurant('Kargil', 'Hakka Noodles')

#Printing attributes Indivisuali
print(restaurant.restaurant_name)
print(restaurant.cuisine)
print('-' *10)
#calling the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

#i have to make new variables to store the new instances values
restaurant1 = Restaurant('FoodEx', 'Indian')
restaurant2 = Restaurant('J14', 'German')
restaurant3 = Restaurant('Johns Kitchen', 'Mix Country')
print('-'*10)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print('-'*10)
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
print('-' *10)
restaurant3.describe_restaurant()
restaurant3.open_restaurant()




