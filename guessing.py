import random 
jackpot = random.randint(1,100)
counter = 0
guess= int(input("chal guess kar: "))
counter += 1 
while guess != jackpot:
    if guess < jackpot:
        print ("guess higher")
    else:
        print ("guess lower")
    guess = int(input("chal guess kar: "))  
    counter+=1

print("sahi jawab")
print("you took",counter,"attempts")