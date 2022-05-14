class Card():
    def __init__(self, name):
        self.name = name
        
    def use(self, user, target):
        print(f"{user.name} used the punch card")
        user.dealDamage(target,5)

