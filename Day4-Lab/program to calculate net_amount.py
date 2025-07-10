# program to calculate net amount after discount based on toy type and order amount

# taking product code and order amount as input
product_code = int(input("Enter the product code(1.Battery-based, 2.Key-based, 3.Electrical Charging):"))
order_amount = float(input("Enter the order amount of the product: "))

#initialize discount
discount = 0

#check conditions based on product code
if product_code == 1:   #battery-based toys
    if order_amount > 1000:
        discount = 0.10 * order_amount
elif product_code == 2:  #Key-based toys
    if order_amount > 100:
        discount = 0.5 * order_amount
elif product_code == 3:  #Electrical-based toys
    if order_amount > 500:
        discount = 0.10 * order_amount
else:
    print("Inavlid Product Code")

#calculate net amount
net_amount = order_amount - discount

#print the net amoount
print(f"The net amount to be paid: {net_amount:.2f}")


                   
