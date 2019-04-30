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
        self.relationship_type_dictionary()
        # if len(self.relationship_type) == 3:
        #     if self.relationship_type == "*--":
        #         self.compo_1_to_1.append(self.class_name)
        #     if self.relationship_type == "o--":
        #         self.aggr_1_to_1.append(self.class_name)
        #     if self.relationship_type == "<--":
        #         self.association_list.append(self.class_name)
        #     if self.relationship_type == "<..":
        #         self.dependency_list.append(self.class_name)
        # # elif len(self.relationship_type) > 3:
        #     if self.relationship_type == '"1"*--"many"':
        #         self.compo_1_to_many.append(self.class_name)
        #     if self.relationship_type == '"1"o--"many"':
        #         self.aggr_1_to_many.append(self.class_name)

    def relationship_type_dictionary(self):
        dictionary = {"*--": "self.compo_1_to_1.append(self.class_name)",
                      "o--": "self.aggr_1_to_1.append(self.class_name)",
                      "<--": "self.association_list.append(self.class_name)",
                      "<..": "self.dependency_list.append(self.class_name)",
                      '"1"*--"many"': "self.compo_1_to_many.append(self.class_name)",
                      '"1"o--"many"': "self.aggr_1_to_many.append(self.class_name)"}
        key = self.relationship_type
        if key in dictionary:
            exec(dictionary[key])

    def __str__(self):
        self.identify_relationship_type()
        result = ""
        if self.compo_1_to_1 is not None:
            for i in self.compo_1_to_1:
                result += "        # self. my_" + i.lower() + " -> " + i\
                        + "\n" + "        self." + i.lower() + " = " + "None \n"
        if self.compo_1_to_many is not None:
            for i in self.compo_1_to_many:
                result += "        # self. my_" + i.lower() + ": list" + " -> "\
                          + i + "\n" + "        self." + i.lower() + " = "\
                          + "None\n"
        return  result
