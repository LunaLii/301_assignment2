class MethodMaker:
    def __init__(self, new_name):
        self.name = new_name

    def __str__(self):
        return '    def ' + self.name + '(self):\n        # Todo: inco' \
                                               'mplete\n        pass\n'
