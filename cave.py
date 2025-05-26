class Cave():
    def __init__(self, type):
        self.type = type
        self.description = None
        self.linked_caves = {}
    
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    