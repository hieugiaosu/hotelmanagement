class Drink:
    def __init__(self,drinkid, name, price):
        self.id = drinkid
        self.name = name
        self.price = int(price)
    def cost(self, soluong):
        return self.price*int(soluong)