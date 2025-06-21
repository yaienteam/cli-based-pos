



def addproduct(productname):
    

    with open('products.txt','a') as file:
        file.write(f"{productname}\n")
        print("PRODUCT ADDED SUCCESSFULLY! ")
    
    
        