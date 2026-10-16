from p91_multilevel import Product

class Order(Product):
    type = "Order_class"
    def __init__(self,Product_Name,price,order_id, quantity):
        super().__init__(Product_Name,price)
        self.order_id=order_id
        self.quantity=quantity
    def show_Order_details(self):
        super().show_product_details()
        print(f"Class name : {Order.type}")
        print(f"order_id : {self.order_id}")
        print(f"quantity : {self.quantity}")