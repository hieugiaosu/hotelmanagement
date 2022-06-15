class Drink:
    def __init__(self,drinkid, name, price):
        self.id = drinkid
        self.name = name
        self.price = price
    def cost(self, soluong):
        return self.price*soluong