#Song libery with Capitalize words
song_libarey = ("Qawwal", "Rock", "Pop", "DHH", "Romantic", "Rage")

#user input and immediatly .capitalize it to match The playlist
user_song = input("Select A song: ").capitalize().strip()
user_song2 = input("Slect Second Song: (For No interruption:  )").strip().capitalize()
#For more simple to focus on the words
print("-"*50)
#Checking Both input are 'in' song_libery
if user_song in song_libarey and user_song2 in song_libarey:
    '''if user enter both song match the libarey it will print this'''
    print("Great: Both Song in Our Playlist! ")
    
elif user_song in song_libarey or user_song2 in song_libarey:
    '''if User one don't match with the libery it will print this'''
    print("Your select one song corretly: But the other one is not in our programe ")
else:
    '''And if user both song don't match to the libery it will print this'''
    print("Can't Find Those Song In Libery")
print("-"*50)
#This will show the User Libery so Next time user What songs are in the libary
print(song_libarey)