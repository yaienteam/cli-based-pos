
def manage_products():
    print("Managing Products")
def add_product():
    print("Adding Product")


def view_products():
    print("Viewing Products")

def update_or_delete_product():
    print("Update/Delete Product")

def signin():
    print("In Sign in")
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open('password.txt','r') as file:
        for line in file:
            fileusername,filepassword=line.strip().split(',')
            if username==fileusername and password==filepassword:
                return True
            return False
    

def main():
    while True:

        start = input("Press 'Enter key' to start the POS System: ")
        if start == "":
            break
        else:
            print("Press Enter to start.")

    if signin():
         print("Login successful!")
         while True:
            print(" Main Menu — select an option from the following:")
            print("1. Manage Products")
            print("2-Add Product")
            print("3 View Product")
            print("4.   (Reserved for Future Feature)")
            print("5. Update/Delete Product")

            choice = input("Enter your choice (1-5): ")





            if choice == '1':
             manage_products()
            elif choice == '2':
                add_product()
            elif choice == '3':
             view_products()
            elif choice == '5':
             update_or_delete_product()
            else:
             print(" Please select a option from these to start  (1-5).")
    else:
        print("INVALID USERNAME PASSWORD")



if __name__ == "__main__":
    main()
