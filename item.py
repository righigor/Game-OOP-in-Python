class Item():
    def __init__(self, item):
        self.name = item
        self.description = None

    def set_descreption(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def describe(self):
        print (self.description)

    def get_details(self):
        print(self.name)
        print("-------------------")
        print(self.description)

    

