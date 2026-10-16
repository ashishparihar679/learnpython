from p92 import Order
class Delivery(Order):
    type = "Delivery_class"
    def __init__(self,Product_Name,price,order_id, quantity,delivery_address, delivery_status):
        super().__init__(Product_Name,price,order_id, quantity)
        self.delivery_address=delivery_address
        self.delivery_status=delivery_status
       
    def show_Delivery_details(self):
        super().show_Order_details()
        print(f"Class name : {Delivery.type}")
        print(f"delivery_address : {self.delivery_address}")
        print(f"delivery_status : {self.delivery_status}")

Obj=Delivery("Laptop",50000,101,5,"Bhopal","Pending")
Obj.show_Delivery_details()
