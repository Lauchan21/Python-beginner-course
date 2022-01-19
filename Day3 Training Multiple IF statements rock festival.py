print ("Welcome to the rock festival!")
height = int(input("What is your height in cm? "))
bill = 0
    
if height >= 160:
    print("You can access the event!")
    age = int(input("What is your age? "))
    if age >= 18:
        bill = 150
        print("Adult ticket tickets are $150.")
        
        wants_Ethereum_NFT = input("Do you want an Ethereum NFT? Y or N. ")
        if wants_Ethereum_NFT == "Y":
            bill = bill + 500
        
        print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you are not allowed to enter")