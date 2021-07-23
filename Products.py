class Products:
    def __init__(self, id, name, price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
      return f'id: {self.id} name:{self.name} price:{self.price}  quantity:{self.quantity}'