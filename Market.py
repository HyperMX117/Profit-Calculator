
def CEP():
    print("INPUT THE FOLLOWING")
    input_PriceTag = float(input("Price Tag: "))
    input_Quantity = int(input("Quantity: "))
    input_SellPrice = float(input("Sell Price: "))

    investmentCost = float(input_PriceTag * input_Quantity)
    earning = float(input_Quantity*input_SellPrice)
    profit = float((input_SellPrice*input_Quantity) - investmentCost)
    percent = float((profit / investmentCost)*100)
    print("-------------------")
    print("Cost: ", investmentCost)
    print("Earned: ",round(earning, 2))
    print("Profit: ", round(percent, 2),"%"," (",round(profit, 2),")")
    
    again = input("\nCompute Again? [Y/N]: ")
    if again == "Y" or again == "y":
        print("-------------------")
        CEP()
    else: print("Program End..")

CEP()