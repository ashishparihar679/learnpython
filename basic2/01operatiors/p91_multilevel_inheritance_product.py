class Product:
    type = "Product class"
    def __init__(self,Product_Name,price):
        self.Product_Name=Product_Name
        self.price=price
    def show_product_details(self):
        print(f"Class name : {Product.type}")
        print(f"Product_Name : {self.Product_Name}")
        print(f"Price : {self.price}")