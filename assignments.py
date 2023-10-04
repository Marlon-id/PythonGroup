import os

def main():
    if not os.path.exists("NewJeans.txt"):
        with open ("NewJeans.txt", "w") as f:
            f.write(f"1\nID000,admin,admin,a\n")
            
    
    if not os.path.exists("suppliers.txt"):
        with open ("suppliers.txt","w") as f:
            f.write(f"1\n")
        print("\nSupplier text file created\n")

    if not os.path.exists("hospitals.txt"):
        with open ("hospitals.txt","w") as f:
            f.write(f"1\n")
        print("\nHospital text file created\n")

    login()

def read_data(filename):
    with open(filename,"r") as f:
            user_list = []
            for list in f:
                user = list.strip().split(",")
                user_list.append(user)
    return user_list

def save_data(filename, list):
    with open(filename, "w") as f:
        for item in list:
            f.write(",".join(item) + "\n")

def yes_no_question():
    print()
    while True:
            response = input("Do you want to continue? (y/n): ").lower()
            if response in ["y","n"]:
                return response
            else:
                print("Please enter a valid response.")
    
def login():
    user_list = read_data("Newjeans.txt")
                
    print("\n"+"="* 20 + "\n" +"..Login..".center(20)+ "\n" + "="* 20 + "\n")
    
    tries = 3

    while tries > 0:
        
        username = input("Please enter username: ").strip()
        password = input("Please enter password: ").strip()

        valid_user = False
        c = 0 
        
        for i in range(1,len(user_list)):
            if username == user_list[i][1]:
                valid_user = True
                index = user_list.index(user_list[i])
                c += index
                break
            else:
                continue
        if valid_user:
            if password == user_list[c][2]:
                print("\nLogin Successful\n")
                print(f"Welcome, {user_list[c][1]}\n")
                if (user_list[c][3].strip()) == "s":
                    print("Entering user menu...\n")
                    user_menu()
                    break
                elif (user_list[c][3].strip()) == "a":
                    print("Entering admin menu...\n")
                    admin_menu()
                    break
            else:
                print("\nWrong password...\n")
                tries -= 1    
                print(f"Chance left = {tries}\n")
        else:
            print("\nInvalid username. Please try again.\n")
            tries -= 1    
            print(f"Chance left = {tries}\n")
    if tries == 0:
        exit("\n.\n.\n.\nIncorrect credentials, exiting program.")           

def user_lists():
    user_list = read_data("Newjeans.txt")
        
    print("\n"+("=" * 57))
    print("|","User ID".center(25),"|","Username".center(25),"|")
    print("=" * 57)

    for user in sorted(user_list[2:len(user_list)]):
        print("|",user[0].center(25),"|" ,user[1].center(25),"|")
    print("=" * 57 ) 

def supplier_lists():
    supplier_list = read_data("suppliers.txt")
    
    print("\n"+("=" * 85))
    print("|","Supplier ID".center(25),"|","Supplier Name".center(25),"|","Supplier Address".center(25),"|")
    print("=" *85)

    for supplier in sorted(supplier_list[1:]):
        print("|",supplier[0].center(25),"|" ,supplier[1].center(25),"|",supplier[2].center(25),"|")
    print("=" *85)   

def hospital_lists():
    hospital_list = read_data("hospitals.txt")
    
    print("\n"+("=" * 85))
    print("|","Supplier ID".center(25),"|","Supplier Name".center(25),"|","Supplier Address".center(25),"|")
    print("=" *85)

    for hospital in sorted(hospital_list[1:]):
        print("|",hospital[0].center(25),"|" ,hospital[1].center(25),"|",hospital[2].center(25),"|")
    print("=" *85)   

def admin_menu():
    while True:
        print(("="* 30 )+ "\n"+ ("Admin Menu".center(30)+ "\n" + ("="* 30)))
        print("0 Exit")
        print("1 User management")
        print("2 Inventory Management")
        print("3 Supplier Management")
        print("4 Hospital Management")
        
        print(("="* 30) + "\n")

        while True:
            response = input("Please enter a number: ")
            if response in ["0","1","2","3","4"]:
                break
            else:
                print("Please enter a valid number")
        
        if response == "0":
            exit("\n"+((".".center(30)+"\n")*3) + "=" * 30 + "\n" +"...End of Program...".center(30) +"\n"+ "=" * 30)
        elif response == "1":
            user_management()
        elif response == "2":
            inventory_management()
        elif response == "3":
            supplier_management()
        elif response == "4":
            hospital_management()

def user_management():
    while True:
        print("\n" + ("="* 30) + "\n" + "User Management Menu".center(30) + "\n" +( "="* 30) + "\n" + "0 Return to Admin Menu\n" + "1 User List\n" + "2 Add new user\n" + "3 Delete a user\n" + "4 Edit user details\n" + ("="* 30) + "\n" )

        while True:
            response = input("Please enter a number: ")
            if response in ["0","1","2","3","4"]:
                break
            else:
                print("Please enter a valid number.")
            
            
        if response == "0":
            print("\n" * 2)
            print("=" * 30)
            print("..Returning to Admin Menu ...".center(30))
            print("=" * 30)
            print()
            break
        elif response == "1":
            view_user_lists()

        elif response =="2":
            add_new_user()

        elif response == "3":
            delete_user()
        elif response == "4":
            edit_user_details()

def add_new_user():
    while True:  
        userlist = read_data("Newjeans.txt")
        
                
        number = int(userlist[0][0])
        userID = "ID" + (str(number).zfill(3))
        userlist[0][0]= str((number)+1)
        while True:
            repeat = False
            name = input("\nPlease enter username: ").strip()
            for i in range(2,len(userlist)):
                if name == userlist[i][1]:
                    repeat = True
                    break
            if repeat:
                    print("Username exist. Please enter another name.")
            else:
                break   
        password = input("Please enter user password: ")
        while True:
            account_type = input("Please enter user account type (a / s):  ").lower()
            if account_type in ["a","s"]:
                break
            else:
                print("Please enter a valid input.")
                
        list = [userID,name,password,account_type]
        userlist.append(list)
        
        save_data("NewJeans.txt", userlist)
        
        print(f"\nNew user [{name}] added.")
        
        response = yes_no_question()
        
        if response == "n":
            print("\nReturning to admin menu..")
            break

def view_user_lists():
    user_lists()
    input("\nPress 'Enter'to exit: ")

def delete_user():
    user_lists()
    while True:
        user_list = read_data("Newjeans.txt")
        
        remove_user = input("\nPlease enter username you wish to delete: ").strip()
        print()
        
        account = False
        
        for user in user_list[2:]:
            if remove_user == user[1]:
                account = True
                while True:
                    confirm = input(f"Please confirm to delete account: {user[0]}: {user[1]} (y / n): ")
                    if confirm in ["y","n"]:
                        break
                    else:
                        print("Please enter a valid input")
            
                if confirm == "y":
                    user_list.remove(user)
                    print("\nAccount deleted.")
            
        if account == False:
            print("Account doesn't exist")

        save_data("Newjeans.txt", user_list)
        
        response = yes_no_question()
        
        if response == "n":
            print("\nReturning to menu...")
            break

def edit_user_details():
    user_lists()
    
    while True:
        user_list = read_data("Newjeans.txt")
        
        search = input("\nEnter user ID: ").strip()
        
        account = False
        num = 0
        
        for user in user_list[2:]:
            if search == user[0]:
                num += user_list.index(user)
                account = True
                break
                    
        if account:
            print(f"\nEditing details for user: [{user_list[num][1]}]")
            print("\n" + ("=" * 30))
            print("0 Back to Menu")
            print("1 Edit username")
            print("2 Edit password")
            print(("=" * 30) + "\n")
            
            while True:
                edit = input("Please enter which information to edit: ")
                print()
                if edit in ["0","1","2"]:
                    break
                else:
                    print("Enter a valid number")
                    
            if edit == "0":
                print("\nReturning to User Management Menu...\n")
                break
            
            elif edit == "1" :
                while True:
                    repeat = False
                    new_username = input("\nPlease enter new username: ").strip()
                    for i in range(2,len(user_list)):
                        if new_username == user_list[i][1]:
                            repeat = True
                            break
                    if new_username == user_list[num][1]:
                        print("\nNew username same with current username. Please try again.")
                    elif repeat:
                            print("Username exist. Please enter another name.")
                    else:
                        break
                while True:
                    confirm = input(f"Please confirm below changes ({user_list[num][1]} --> {new_username}) (y / n): ")
                    if confirm in ["y","n"]:
                            break
                    else:
                        print("Please enter a valid response")
                if confirm == "y":
                    user_list[num][1] = new_username
                    print(f"Username changed to {new_username}!")
                else:
                    pass
            elif edit == "2" :
                old_password = input("Please enter current password: ").strip()
                new_password = input("Please enter new password: ").strip()
                if old_password != user_list[num][2]:
                    print("Incorrect current password. Please try again.")
                else:
                    user_list[num][2] = new_password
                    print(f"Password changed successfully")

        else:
            print("\nUsername does not exist..")

        if account:
            save_data("NewJeans.txt", user_list)

        response = yes_no_question()
                
        if response == "n":
            print("\nReturn to User Management Menu")
            break

def supplier_management():
    while True:
        print("\n" + ("="* 30))
        print("Supplier Management Menu".center(30))
        print(("="* 30))
        print("0 Return to Admin Menu")
        print("1 Supplier List")
        print("2 Add new supplier")
        print("3 Delete a supplier ")
        print("4 Edit supplier details")
        print(("="* 30) + "\n")

        while True:
            response = input("Please enter a number: ").strip()
            if response in ["0","1","2","3","4"]:
                break
            else:
                print("Please enter a valid number.")
            
        if response == "0":
            print("\n" * 2)
            print("=" * 30)
            print("..Returning to Admin Menu ...".center(30))
            print(("=" * 30) + "\n")
            break
        elif response == "1":
            view_supplier_lists()

        elif response =="2":
            add_new_supplier()

        elif response == "3":
            delete_supplier()
        elif response == "4":
            edit_supplier_details()

def add_new_supplier():
    while True:  
        supplierlist = read_data("suppliers.txt")
                
        number = int(supplierlist[0][0])
        supplierID = "SP" + (str(number).zfill(3))
        supplierlist[0][0]= str((number)+1)
        while True:
            repeat = False
            name = input("\nPlease enter supplier name: ").strip()
            for i in range(1,len(supplierlist)):
                if name == supplierlist[i][1]:
                    repeat = True
                    break
            if repeat:
                    print("Supplier name exist. Please enter another name.")
            else:
                break   

        address = input("Please enter supplier address: ")
                
        list = [supplierID,name,address]
        supplierlist.append(list)
        
        save_data("suppliers.txt", supplierlist)
        print(f"\nSupplier [{name}] added")
        
        response = yes_no_question()
        
        if response == "n":
            print("\nReturning to admin menu..")
            break

def view_supplier_lists():
    while True:
        supplier_lists()
        input("Press 'Enter'to exit: ")
        break
    
def delete_supplier():
    while True:
        supplier_list = read_data("suppliers.txt")
            
        supplier_lists()
        
        remove_supplier = input("\nPlease enter supplier name you wish to delete: ").strip()
        print()
        
        account = False
        
        for supplier in supplier_list[1:]:
            if remove_supplier == supplier[1]:
                account = True
                print("Account exists\n")
                while True:
                    confirm = input(f"Please confirm to delete account for: {supplier[0]} : {supplier[1]} ( y / n): ")
                    if confirm in ["y","n"]:
                        break
                    else:
                        print("Please enter a valid input")
            
                if confirm == "y":
                    supplier_list.remove(supplier)
                    print("\nAccount deleted.")
            
        if account == False:
            print("Account does not exist")

        save_data("suppliers.txt", supplier_list)
        
        response = yes_no_question()
        
        if response == "n":
            print("\nReturning to menu...")
            break

def edit_supplier_details():
    supplier_lists()
    
    while True:
        supplier_list = read_data("suppliers.txt")
        
        account = False
        num = 0
        
        while True:
            search = input(("\nEnter supplier code: ")).strip()
            
            for supplier in supplier_list[1:]:
                if search == supplier[0]:
                    num += supplier_list.index(supplier)
                    account = True
                    break
                    
            if account:
                print("\nSupplier exists!")
                print("\n"+("=" * 30))
                print("0 Back to Menu")
                print("1 Edit Supplier name")
                print("2 Edit supplier address")
                print(("=" * 30) + "\n")
                
                while True:
                    edit = input("Please enter which information to edit: ")
                    if edit in ["0","1","2"]:
                        break
                    else:
                        print("Enter a valid number")
                        
                if edit == "0":
                    print("\nReturning to Supplier Management Menu...\n")
                    break
                elif edit == "1" :
                    new_supplier_name = input("\nPlease enter new supplier name: ")
                    while True:
                        confirm = input(f"Please confirm below changes ({supplier_list[num][1]} --> {new_supplier_name}) (y / n): ")
                        if confirm in ["y","n"]:
                            break
                        else:
                            print("Please enter a valid response")
                    if confirm == "y":
                        supplier_list[num][1] = new_supplier_name
                    else:
                        pass
                elif edit == "2" :
                    new_supplier_address = input("Please enter new supplier address: ")
                    while True:
                        confirm = input(f"Please confirm below changes ({supplier_list[num][2]} --> {new_supplier_address}) (y / n): ")
                        if confirm in ["y","n"]:
                            break
                        else:
                            print("Please enter a valid response")
                    if confirm == "y":
                        supplier_list[num][2] = new_supplier_address
                    else:
                        pass
            else:
                print("Supplier does not exist")
            if account:
                save_data("suppliers.txt", supplier_list)
            break
        
        response = yes_no_question()      
        
        if response == "n":
            print("\nReturning to Supplier management menu...\n ")
            break

def hospital_management():
    while True:
        print("\n"  + ("=" * 30))
        print("Hospital Management Menu".center(30))
        print("="* 30)
        print("0 Return to Admin Menu")
        print("1 Hospital List")
        print("2 Add new Hospital")
        print("3 Delete a Hospital ")
        print(("="* 30)+"\n")

        while True:
            response = input("Please enter a number: ")
            if response in ["0","1","2","3"]:
                break
            else:
                print("Please enter a valid number.")
            
        if response == "0":
            print("\n"  + ("=" * 30))
            print("..Returning to Admin Menu ...".center(30))
            print(("=" * 30) + "\n")
            break
        elif response == "1":
            print("\n")
            view_hospital_lists()

        elif response =="2":
            add_new_hospital()

        elif response == "3":
            delete_hospital()

def add_new_hospital():
    while True:
        hospital_list = read_data("hospitals.txt")

        number = int(hospital_list[0][0])
        hospitalID = "HS" + (str(number).zfill(3))
        hospital_list[0][0]= str((number)+1)
        hospitalName = input("\nPlease enter hospital name: ").strip()
        hospitalAddress = input("Please enter hospital address: ")
                
        list = [hospitalID,hospitalName,hospitalAddress]
        hospital_list.append(list)
        
        save_data("hospitals.txt", hospital_list)
        print(f"\nHospital [{hospitalName}] added\n")
        
        response = yes_no_question()
        
        if response == "n":
            print("\nReturning to admin menu..")
            break
        
def view_hospital_lists():
    while True:
        hospital_lists()
        input("Press 'Enter'to exit: ")
        break

def delete_hospital():
    hospital_lists()
    while True:
        hospital_list = read_data("hospitals.txt")
            
        remove_hospital = input("\nPlease enter hospital name you wish to delete: ").strip()
        print()
        
        account = False
        for hospital in hospital_list[1:]:
            if remove_hospital == hospital[1]:
                account = True
                print("Account exists")
                while True:
                    confirm = input(f"Please confirm to delete account for: {hospital[0]} , {hospital[1]} ( y / n): ")
                    if confirm in ["y","n"]:
                        break
                    else:
                        print("Please enter a valid input")

                if confirm == "y":
                    hospital_list.remove(hospital)
                    print("Account deleted.")
                
        if not account:
            print("Account does not exist")

        save_data("hospitals.txt", hospital_list)
        
        response = yes_no_question()
        
        if response == "n":
            print()
            print("Returning to menu...")
            break

def user_menu():
    while True:

        print(("="* 20) + "\n" + "User Menu".center(20)+"\n" +"0 Exit\n" + "1 Inventory Menu\n" + ("="* 20) + "\n")

        response = input("Please enter a number: ")

        while True:
            if response in ["0","1"]:
                break
            else:
                print("Please enter a valid number")
        
        if response == "0":
            print(".\n".center(30))
            print(".\n".center(30))
            print(".\n".center(30))
            print("=" * 30)
            print("...End of Program...".center(30))
            print("=" * 30)
            exit()
        else:
            inventory_management()
            break

def inventory_management():
    while True:
        print("Inventory")
        break

main()