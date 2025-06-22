
from addproduct import addproduct



def manage_products():
    try:
        with open("products.txt", "r") as file:
            products = file.readlines()
            if not products:
                print("No products available.")
            else:
                print("Product List:")
                for index, product in enumerate(products, start=1):
                    print(f"{index}. {product.strip()}")
                print(f"\nTotal products: {len(products)}")
    except FileNotFoundError:
        print("products.txt not found.")

def add_product():
    while True:
     productname=input("Enter Producr Name 0R -1 to exit: ")
   
     if (productname=="-1"):
      break
     else:
        addproduct(productname) 

def view_products():
    try:
        with open("products.txt", "r") as file:
            products = file.readlines()
            if not products:
                print("No products found.")
            else:
                for index, product in enumerate(products, start=1):
                    print(f"{index}. {product.strip()}")
    except FileNotFoundError:
        print("products.txt not found.")

def update_or_delete_product():
    try:
        with open("products.txt", "r") as file:
            products = file.readlines()

        if not products:
            print("No products available to update or delete.")
            return

        print("\nProduct List:")
        for index, product in enumerate(products, start=1):
            print(f"{index}. {product.strip()}")

        action = input("\nDo you want to (u)pdate or (d)elete a product? (u/d): ").lower()

        if action not in ['u', 'd']:
            print("Invalid choice.")
            return

        number = input("Enter the product number: ")

        if not number.isdigit() or int(number) < 1 or int(number) > len(products):
            print("Invalid product number.")
            return

        index = int(number) - 1

        if action == 'u':
            new_name = input("Enter the new product name: ")
            products[index] = new_name + "\n"
            print("Product updated successfully.")

        elif action == 'd':
            removed = products.pop(index)
            print(f"Product '{removed.strip()}' deleted successfully.")

        with open("products.txt", "w") as file:
            file.writelines(products)

    except FileNotFoundError:
        print("products.txt not found.")


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
