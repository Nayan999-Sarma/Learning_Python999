lucky_number = 99
rewards = ["Mackbook", "Iphone 17 pro max"]

print("=======WELCOME TO GUESSING GAME========")
print("You Have 5 Chances To Guess The Lucky Number")

for i in range(5):
    
    user = int(input("Guess The Lucky Number"))
    if user == lucky_number:
        print("You Won",rewards)
        break
    else:
        print(f"\n Guess Againg: Attmp {i+1} of 5")

else:
    print("All The Best For Next Time")

