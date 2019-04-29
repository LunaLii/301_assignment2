class AttributeMaker:
    def __init__(self,new_name):
        self.name = new_name

    def __str__(self):
        return '        self.' + self.name + ' = ' + self.name + '\n'

    # def get_length(self):
    #     return len(self.name)
