from attribute_maker import AttributeMaker
from method_maker import MethodMaker
from relationship_maker import RelationshipMaker


class ClassMaker:
    def __init__(self, class_name, new_attributes, new_methods, new_relationships):
        self.name = class_name
        self.attributes = new_attributes
        self.methods = new_methods
        self.relationships = new_relationships
        self.all_my_attributes_name = []
        self.all_my_attributes = []
        self.all_my_methods = []
        self.all_my_relationships = []

    def add_class_attributes(self):
        for an_attribute in self.attributes:
            new_a_name = an_attribute.split(" ")[4]
            new_attribute = AttributeMaker(new_a_name)
            self.all_my_attributes.append(new_attribute)

    def add_class_methods(self):
        for a_method in self.methods:
            new_m_name = a_method[:a_method.index("\n")-2].strip()
            new_method = MethodMaker(new_m_name)
            self.all_my_methods.append(new_method)

    def add_class_relationships(self):
        for a_relationship in self.relationships:
            temp_relationship = a_relationship.split(" ")
            first_c_name = temp_relationship[0]
            second_c_name = temp_relationship[-1].replace("\n","")
            relationship_type = ''.join(temp_relationship[1:-1])
            if first_c_name == self.name:
                the_relationship = RelationshipMaker(second_c_name,relationship_type)
                self.all_my_relationships.append(the_relationship)

    def get_attribute_length(self):
        return len(self.all_my_attributes)

    def get_method_length(self):
        return len(self.all_my_methods)

    def print_class(self):
        result = "class " + self.name + ":"
        result += "\n" + "    def __init__(self"
        for x in self.all_my_attributes:
            result += ", " + x.name
        result += "):\n"
        for x in self.all_my_attributes:
            result += str(x)
        for x in self.all_my_relationships:
            result += str(x)
        if self.get_attribute_length() == 0 and self.get_attribute_length() == 0:
            result += "        pass\n"
        for x in self.all_my_methods:
            result += "\n"
            result += str(x)
        return result
