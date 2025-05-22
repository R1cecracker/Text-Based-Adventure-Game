class Cave():
    def __init__(self, type):
        self.type = type
        self.info = None
        self.linked_caves = {}
    
    def get_info(self):
        return self.info
    
    def set_info(self, info):
        self.info = info

    def get_type(self):
        return self.type

    def info(self):
        print({self.type})

