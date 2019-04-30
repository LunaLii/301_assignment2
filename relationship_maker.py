class RelationshipMaker:
    def __init__(self, second_c_name, relationship_type):
        self.class_name = second_c_name
        self.relationship_type = relationship_type
        self.compo_1_to_1 = []
        self.aggr_1_to_1 = []
        self.compo_1_to_many = []
        self.aggr_1_to_many = []
        self.association_list = []
        self.dependency_list = []

    def identify_relationship_type(self):
        dictionary = self.relationship_type_dictionary()
        key = self.relationship_type
        if key in dictionary:
            exec(dictionary[key])

    def relationship_type_dictionary(self):
        dictionary = {"*--": "self.compo_1_to_1.append(self.class_name)",
                      "o--": "self.aggr_1_to_1.append(self.class_name)",
                      "<--": "self.association_list.append(self.class_name)",
                      "<..": "self.dependency_list.append(self.class_name)",
                      '"1"*--"many"': "self.compo_1_to_many.append"
                                      "(self.class_name)",
                      '"1"o--"many"': "self.aggr_1_to_many.append"
                                      "(self.class_name)"}
        return dictionary

    def __str__(self):
        self.identify_relationship_type()
        result = ""
        if self.compo_1_to_1 is not None:
            for i in self.compo_1_to_1:
                result += "        # self. my_" + i.lower() + " -> " + i\
                        + "\n" + "        self." + i.lower() + " = " + "None\n"
        if self.compo_1_to_many is not None:
            for i in self.compo_1_to_many:
                result += "        # self. my_" + i.lower() + ": list" + \
                          " -> " + i + "\n" + "        self." + i.lower() \
                          + " = " + "None\n"
        return result
