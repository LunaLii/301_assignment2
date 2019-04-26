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
        if len(self.relationship_type) == 3:
            if self.relationship_type == "*--":
                self.compo_1_to_1.append(self.class_name)
            if self.relationship_type == "o--":
                self.aggr_1_to_1.append(self.class_name)
            if self.relationship_type == "<--":
                self.association_list.append(self.class_name)
            if self.relationship_type == "<..":
                self.dependency_list.append(self.class_name)
        elif len(self.relationship_type) > 3:
            if self.relationship_type == '"1"*--"many"':
                self.compo_1_to_many.append(self.class_name)
            if self.relationship_type == '"1"o--"many"':
                self.aggr_1_to_many.append(self.class_name)
