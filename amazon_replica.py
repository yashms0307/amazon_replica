

#                                    A M A Z O N  ooo  R E P L I C A


#@Product List
shopping = [{"id": 1001, "Name": "HP", "Available": 100, "Price": 160000, "Discounted_Price": 150000},
            {"id": 1002, "Name": "Wrogn", "Available": 100, "Price": 800, "Discounted_Price": 750},
            {"id": 1003, "Name": "Chips", "Available": 100, "Price": 40, "Discounted_Price": 38},
            {"id": 1004, "Name": "iPhone", "Available": 100, "Price": 60000, "Discounted_Price": 58000}]

shopping1 = shopping
temp = []
order = ""

#                                           Admin's Place


#@Login Window
def adminLoginWindow():
    print("=====================")
    print("1.Display Product")
    print("2.Add Product")
    print("3.Remove Product")
    print("4.Products goods available")
    print("5.Logout")
    print("=====================")

#@Display Product
def adminDisplayMenuWindow():
    print("Id\tName\tAvailable\tPrice\tDiscounted Price")
    print("====================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}\t{d["Discounted_Price"]}')


#@Add Products
def addproducts():
    n = int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        new_id = int(input("Enter id : "))
        new_Name = input("Enter Name : ")

        new_Available = int(input("Enter Available : "))
        new_Price = int(input("Enter Price : "))
        new_original = int(input("Enter the Discounted Price : "))
        d = [{"id": new_id, "Name": new_Name, "Available": new_Available, "Price": new_Price,
              "Discounted_Price": new_original}]
        shopping.extend(d)
        adminDisplayMenuWindow()


#@Delete Products
def removeproducts():
    dressId = int(input("Enter the id need to be deleted : "))
    found = False
    for d in shopping1:
        found = d["id"] == dressId
        if found != True:
            temp.append(d)
            continue
        if found == True:
            d["Available"] -= 1
    print("Deleting item....")
    if len(temp) == d:
        print(f"{dressId} not found")
    else:
        print(f"{dressId}'s one available is removed from the list")
    adminDisplayMenuWindow()


#@Products Available
def availableproducts():
    Total = 0
    print("\n")
    for d in shopping:
        print(f'{d["Name"]} = {d["Available"]}')
        Total += (d["Available"])
    print("\nTotal available goods is : ", Total)

#@Logout
def logoutwindow():
    login()

#@Options available to Admin
def adminOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        addproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 3:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        removeproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 4:
        availableproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 5:
        logoutwindow()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()

#                                          User's Place

#@Login
def userLoginWindow():
    print("=====================\n")
    print("1.Display Product")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
    print("\n======================")

#@Display Products
def userDisplayMenuWindow():
    print("Id\tName\tAvailable\tPrice")
    print("===================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')

#@ User ID
def user_id():
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))

#@ Placing Order
def placeOrder():
    order_number = 10
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))

    for d in shopping:
        if d["id"] == p_id:
            print("\nId\tName\tAvailable\tPrice")
            print("=============================================================")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            order = '{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")

            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
                order_number += 1
                print("Your order number is : ", order_number)
                d["Available"] -= 1
                break

            elif conform == 'N' or conform == 'n':
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break

    if d["id"] != p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        user_id()
    print("\nAvailable products : \n")
    userDisplayMenuWindow()


#@Cancelling Order
def cancelOrder():
    found = False
    temp = []
    order_id = input("Enter the order id : ")
    for d in shopping:
        found = d["id"] == order_id
        if found != True:
            temp.append(d)
    if len(temp) == d:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')

#@Options Displayed to User
def userChoiceOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        userDisplayMenuWindow()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 2:
        placeOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 3:
        cancelOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 4:
        logoutwindow()
    else:
        print("Invalid Choice. Please enter valid choice")


#                                               Login


#@Login
def login():
    tp = input("Login Admin/Login User [Type admin to Login in the Admin/ Type user to Login in the User] : ")
    if tp == 'admin':
        print("Password Hint - admin")
        password = input("Enter the password : ")
        if password == "admin":
            adminLoginWindow()
            adminOptions()
        else:
            print("Invalid password. Please enter valid password")
            
#@Asking User for Personal Information
    elif tp == 'user':
        cust_name = input("Enter Name: ")
        cust_email = input("Enter Email: ")
        cust_address = input("Enter Address: ")
        print("==============================")
        print("")
        print("User Details: ")
        
        print("Customer Name:",cust_name)
        print("Customer Email:",cust_email)
        print("Customer Address:",cust_address)
        print("")
        print("==============================")
        
        print("Password Hint - user")
        password = input("Enter the password : ")
        if (password == "user"):
            userLoginWindow()
            userChoiceOptions()
        else:
            print("Invalid password. Please enter valid password")
    else:
        print("Invalid user type. Enter valid user type")


login()


#                                    A M Z O N  ooo R E P L I C A






