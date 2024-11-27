class Item():

    def __init__(self, name, buy_threshold, current_ammount=0):
        self.name = name
        self.buy_threshold = buy_threshold
        self.current_ammount = current_ammount
        
    def use(self, ammount=1):
        if self.current_ammount > 1:
            return
        self.current_ammount -= ammount
        return f"Used {ammount} of {self}"

    def buy(self, ammount):
        self.current_ammount += ammount


class Pantry():


    def __init__(self, items):

