name=input("Enter your name: ")
print(f"Hello {name} I am an AI bot which will check your mood.")
mood=input("Please enter your mood(good/bad): ").lower()
while True:
    if mood=="good":
        print("I am glad to hear that")
        break
    elif mood=="bad":
       print("I am sorry to hear that")
       break
    else:
        print("Please enter either good or bad")
        break
print(f"It was nice to meet you {name}. Have a great day")