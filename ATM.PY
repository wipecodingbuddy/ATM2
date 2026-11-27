print("welcome to abc bank : ")
balance = 10000
pin = 1234
while True:
    attempts = 0
    while attempts<3:
        userpin = int(input("enter the pin : "))

        if(userpin == pin):
            print("correct pin ")
            break
        else:
            attempts = attempts + 1
            print("wrong pin, attempts left = ",3-attempts)

    if(userpin!=pin and attempts == 3):
        print("your ac has been blocked ")
        break


    print("PRESS 1 TO KNOW YOUR CURRENT BALANCE ")
    print("PRESS 2 TO add money ")
    print("PRESS 3 TO WITHDRAW MONEY")
    print("PRESS 4 TO change pin ")
    press = int(input("enter what you want to do : "))


    if(press==1):
        print("your current balane is : ",balance)
                                                

    elif(press==2):
        money = int(input("enter the money you would like to add : ")) 
        balance = balance + money
        print("balance after addinhg money is : ",balance)

    elif(press == 3):
        withdraw = int(input("enter the amount to withdraw : "))

        if(withdraw<=(balance-1000)):
            balance = balance - withdraw
            print("balnce after withddrawl is : ",balance)

        else:
            print("there should be at least 1000 rs in the ac ")      

    elif(press == 4):
        chances = 0
        while chances<3:
            oldpin = int(input("enter the old pin : "))
            if(oldpin == pin):
                newpin = int(input("enter the new pin : "))
                pin = newpin
                print("your pin hsa been changed ")
                break

            else:
                chances = chances + 1
                print("wrong pin, chances left = ",3-chances)

        if(chances==3 and oldpin!=pin):
            print("your ac has been blocked")
            break

    else:
        print("invalid operation ")

    choice = input("do you want to continuw : (yes or no) : ")
    if(choice.lower()=="no"):
        print("thanks for banking with us ")
        break