
class Burger:
    base_price: float = 150.0
    base_ingredients: list[str] = ['buns', 'patty']
    options: list[str] = ['cheese', 'lettuce', 'tomatoes']

    def __init__(self):
       self.ingredients =self.base_ingredients.copy()
       self.price = self.base_price
    
    def add_cheese(self):
        self.ingredients.append('cheese')
        self.price += 50
    
    def add_lettuce(self):
        self.ingredients.append('lettuce')
        self.price += 20

    def add_tomatoes(self):
        self.ingredients.append('tomatoes')
        self.price +=  10
    
    def return_burger(self):
        return self.ingredients
    
    def return_price(self):
        return self.price  
    

if __name__ == "__main__":
    burger = Burger()
    burger.add_cheese()
    burger.add_lettuce()
    burger.add_tomatoes()
    print(burger.return_burger())
    print(burger.return_price())