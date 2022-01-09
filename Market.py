def wilRepeat():
    again = input("\nBack To Menu? [Y/N]: ")
    if again == "Y" or again == "y":
        print("__________________________________________________\n")
        main()
    else: print("Program End..")
def Default():
    print("--------------------[Default]--------------------")
    input_PriceTag = float(input("[INPUT] Price Tag: "))
    input_Quantity = int(input("[INPUT] Quantity: "))
    input_SellPrice = float(input("[INPUT] Sell Price: "))

    #Computation
    investmentCost = float(input_PriceTag * input_Quantity)
    earning = float(input_Quantity*input_SellPrice)
    profit = float((input_SellPrice*input_Quantity) - investmentCost)
    percent = float((profit / investmentCost)*100)
    market_buyersPay = (input_SellPrice * 0.15)+input_SellPrice

    #Output
    print("\n[OUTPUT] Buyers Pay (For Each Item): ",round(market_buyersPay,2))
    print("[OUTPUT] Investment: ", round(investmentCost,2))
    print("[OUTPUT] Earning: ",round(earning, 2))
    print("[OUTPUT] Profit: ", round(percent, 2),"%"," (",round(profit, 2),")")
    print("-------------------------------------------------")
    wilRepeat()
def Percent():
    print("---------------[Profit by Percent]---------------")
    input_PriceTag = float(input("[INPUT] Price Tag: "))
    input_Quantity = int(input("[INPUT] Quantity: "))
    input_Percent = float(input("[INPUT] Profit Percent: "))

    investmentCost = float(input_PriceTag * input_Quantity)
    percent = input_Percent / 100
    sellPrice = float((input_PriceTag*percent)+input_PriceTag)
    market_buyersPay = (sellPrice * 0.15)+sellPrice
    earning = input_Quantity*sellPrice

    #Output
    print("\n[OUTPUT] Sell Price: ",round(sellPrice, 3))
    print("[OUTPUT] Buyers Pay (For Each Item): ",round(market_buyersPay,2))
    print("[OUTPUT] Investment: ", round(investmentCost,2))
    print("[OUTPUT] Earning: ",round(earning,2)," \n[OUTPUT] Profit",input_Percent,"%: (", round(earning-investmentCost,2),")")
    print("-------------------------------------------------")
    wilRepeat()
def Term():
    print("-----------TERMINOLOGIES-------------")
    print("Price Tag = How much it cost you to purchase a single item\nQuantity = The number of the same item you purchased\nSell Price = The amount you want to gain from selling an item (Fee excluded)")
    wilRepeat()
def main():
    index = int(input("SELECT PROFIT MODE\n1 = By Price\n2 = By Percent\n3 = Info\nInput: "))
    if(index == 1):
        Default()
    elif(index == 2):
        Percent()
    elif(index == 3):
        Term()
    else:
        print("INPUT INVALID")

main()
