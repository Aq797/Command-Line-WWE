from classes.game import player
class items:
    def __init__(self,name,type,description,hit):
        self.name=name
        self.type=type
        self.description=description
        self.hit=hit

    def get_Item_Name(self):
        return self.name

    def get_Item_Type(self):
        return self.type

    def get_Item_Description(self):
        return self.description

    def get_Item_Points(self):
        return self.hit





