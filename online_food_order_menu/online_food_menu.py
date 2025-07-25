#welcome message
print("Welcome to our Hotel")
#variables to store total amount and ordered items
total = 0
order_list = []   #this list will store ordered items and their details
while True:
    #display main menu
    print("\n-------Hotel Menu------")
    print("1. Starter")
    print("2. Drinks")
    print("3. Main Course")
    print("4. Desert")
    print("5. Bill")
#take your choice
    choice = int(input("Select your choice(1-5): "))
     #if user selects starter
    if choice==1:
        print("starters")
        print("1.Finger chips - Rs60")
        print("2.Paneer Tikka - Rs160")
                   
        starter = int(input("Select your choice(1-2): "))
        quantity = int(input("Enter quantity:"))
        if (starter == 1):
            total = total + (60*quantity)
            order_list.append(f"Finger Chips x {quantity} = Rs.{60*quantity}")
            print("Your finger chips will be ready in 10 mins")
        elif (starter == 2):
            total = total + (160*quantity)
            order_list.append(f"Paneer Tikka x {quantity} = Rs.{160*quantity}")
            print("Your paneer tikka will be ready in 10 mins")
        else:
            print("Inavlid choice.Please select a valid choise")
            continue
        #if user selects drinks
    elif choice==2:
          print("Drinks")
          print("1.Mojito - Rs70")
          print("2.Fruit juice - Rs140")

          drinks = int(input("Select your choice(1-2): "))
          quantity = int(input("Enter quantity:"))
          if (drinks == 1):
              total = total + (70*quantity)
              order_list.append(f"Mojito x {quantity} = Rs.{70*quantity}")
              print("Your Mojito will be ready in 10 mins")
          elif (drinks == 2):
              total = total + (140*quantity)
              order_list.append(f"Fruit Juice x {quantity} = Rs.{140*quantity}")
              print("Your Fruit juice will be ready in 10 mins")
          else:
              print("Inavlid choice.Please select a valid choise")
              continue
        #if user selects main course
    elif choice==3:
          print("Main Course")
          print("1.Dal Tadka - Rs100")
          print("2.Veg Kadai - Rs200")

          main_course = int(input("Select your choice(1-2): "))
          quantity = int(input("Enter quantity:"))
          if (main_course == 1):
              total = total + (100*quantity)
              order_list.append(f"Dal Tadka x {quantity} = Rs.{100*quantity}")
              print("Your Dal Tadka will be ready in 10 mins")
          elif (main_course == 2):
              total = total + (200*quantity)
              order_list.append(f"Veg Kadai x {quantity} = Rs.{200*quantity}")
              print("Your Veg Kadai will be ready in 10 mins")
          else:
              print("Inavlid choice.Please select a valid choise")
              continue
     #if user selcts desert
    elif choice==4:
          print("Dessert")
          print("1.Ice Cream - Rs60")
          print("2.Falooda - Rs110")

          dessert = int(input("Select your choice(1-2): "))
          quantity = int(input("Enter quantity:"))
          if (dessert == 1):
              total = total + (60*quantity)
              order_list.append(f"Ice Cream x {quantity} = Rs.{60*quantity}")
              print("Your Ice cream will be ready in 10 mins")
          elif (dessert == 2):
              total = total + (110*quantity)
              order_list.append(f"Falooda x {quantity} = Rs.{110*quantity}")
              print("Your Falooda will be ready in 10 mins")
          else:
              print("Inavlid choice.Please select a valid choise")
              continue
  #if user selects bill
    elif choice==5:
          print("\n-------Oredr Summary---------")
          if len(order_list) == 0:
              print("You have not ordered anything")
        #print all ordered items
          else:
              for item in order_list:
                  print(item)
              print("--------------------------")
              print("Your total bill is: Rs",total)
              print("Thank you for ordering")
              
          break   #exit the while loop
    #if user enters any other number
    else:
        print("Inavlid choice.Please select a valid choise")
        continue

                        
