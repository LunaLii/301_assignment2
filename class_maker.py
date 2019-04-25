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
        self.all_my_attributes = AttributeMaker
        self.all_my_methods = []
        self.all_my_relationships = []

    def add_class_attributes(self):
        pass