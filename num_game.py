import random

def cgame():
    ts=0
    
    while True:
        num=random.randint(1,6)

        user=int(input("Guess the number between 1 to 6 :"))

        print(f"your num {user} = computer {num}")

        if num!=user:
            ts+=user
            print("good go go")
        else:
            print("sorry ,u r out !!")
            break

    print("your score :",ts)
    
cgame()

