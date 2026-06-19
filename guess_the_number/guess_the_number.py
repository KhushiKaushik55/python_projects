print("lets play guess the number...u have to guess my number which is between 1 and 100")
import random
a=random.randint(1,100)
i=0
print("you wil get 5 chances...lets see your skills")
while(i<5):
    b=int(input("Enter your guess"))
    if(a==b):
       print("your guess was right...congo u won")
       break
    elif(b>a):
       print("think of a lower number")
    else:
      print("think of a higher number")
    i+=1
if(a!=b):      
    print("oops better luck next time")
    print("The number was ",a)
