from secrets import choice


print("--------------------------------------------------------------------------------------------")
print("*****************************B I L L - G E N E R A T O R************************************")
print("--------------------------------------------------------------------------------------------\n\n")

print("Enter Details of Customer : ")
Name = input("\tEnter Name of the Customer : ")
Phon = input("\tEnter Customer Phone No. : ")
Add = input("\tEnter Addresss of customer : ")
Item = int(input("\n\tHow many Items Customer Wants to purchase : "))
print("\nNow Enter Items Details : ")
TT = 0
for i in range(Item):
    print("\t\n Enter",i+1,"Items Details")
    IN = input("\tItem Name : ")
    QT = int(input("\tQuantity : "))
    PR = float(input("\tPrice of the Item :"))
    AM = PR + QT
    print("\t\tAmount of the Items is : ",AM  )
    TT = QT +AM
print("\n\nTotal Amount is : ",TT,end=',')
GST = TT*12.33/100
print("GST : ",GST,end=',')
NA = TT + GST
print("Total Payble Amount is : ",NA)
choice = int(input("Press 1 for Premium Customer  \nPress 2 for Normal Customer"))
if (choice==1):
    Dis = NA * 5/100
    NA = NA - Dis
    print("Now after discount Net Payble Amount is :",NA)
else:
    print("Now Net Payble Amount is :",NA)

print("--------------------------------------------------------------------------------------------")
print("********************************* T H A N K - Y O U ****************************************")
print("--------------------------------------------------------------------------------------------\n\n")
