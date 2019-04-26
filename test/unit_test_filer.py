import unittest
from file_reader import FileReader
from class_maker import ClassMaker


class FilerUnitTest(unittest.TestCase):
    def setUp(self):
        self.file = FileReader()

    def test_read_word_file(self):
        actual = self.file.read_word_file("test/test2.docx")
        expect = ["@startuml\n", "ToyBox *-- Toy\n", "\n", "class ToyBox {\n",
                  "    name : String\n", "}\n", "\n", "class Toy {\n", "}\n",
                  "@enduml\n"]
        self.assertEqual(expect, actual, "cannot read word file")

    def test_read_txt_file(self):
        actual = self.file.read_txt_file("test/test2.txt")
        expect = ["@startuml\n", "ToyBox *-- Toy\n", "\n", "class ToyBox {\n",
                  "    name : String\n", "}\n", "\n", "class Toy {\n", "}\n",
                  "@enduml\n"]
        self.assertEqual(expect, actual, "cannot read txt file")

    # def test_get_method_name(self):
    #     class_content = self.file.class_handler("test/uml.txt")
    #     actual_one = self.file.get_methods(class_content[0])
    #     expected_one = ["add_toy", "get_toys"]
    #     actual_two = self.file.get_methods(class_content[1])
    #     expected_two = ["__str__"]
    #     self.assertEqual(expected_one, actual_one, "cannot get method name")
    #     self.assertEqual(expected_two, actual_two, "cannot get method name")

    def test_get_class_name(self):
        self.file.class_handler("test/uml.txt")
        self.file.find_classes()
        actual = []
        for x in self.file.all_my_classes:
            actual.append(x.name)
        expected = ["ToyBox", "Toy"]
        self.assertEqual(expected, actual, "cannot get class name")

    # def test_get_attribute_name(self):
    #     class_content = self.file.class_handler("test/uml.docx")
    #     actual_one = self.file.get_attributes(class_content[0])
    #     expected_one = ["number", "allMyToys"]
    #     actual_two = self.file.get_attributes(class_content[1])
    #     expected_two = ["name", "color", "price"]
    #     self.assertEqual(expected_one, actual_one, "cannot get attribute name")
    #     self.assertEqual(expected_two, actual_two, "cannot get attribute name")
    #
    # def test_get_relationship_one_composition(self):
    #     self.file.class_handler("test/test_relationship.txt")
    #     self.file.get_relationship("ClassA")
    #     actual = self.file.compo_1_to_1
    #     expected = ["ClassB"]
    #     self.assertEqual(expected, actual, "cannot get 1 to 1 composition")
    #
    # def test_get_relationship_many_composition(self):
    #     self.file.class_handler("test/test_relationship.txt")
    #     self.file.get_relationship("ToyBox")
    #     actual = self.file.compo_1_to_many
    #     expected = ["Toy"]
    #     self.assertEqual(expected, actual, "cannot get 1 to many composition")
    #
    # def test_get_relationship_many_aggregation(self):
    #     self.file.class_handler("test/test_relationship.txt")
    #     self.file.get_relationship("ClassC")
    #     actual = self.file.aggr_1_to_many
    #     expected = ["ClassD"]
    #     self.assertEqual(expected, actual, "cannot get 1 to many aggregation")
    #
    # def test_get_relationship_one_aggregation(self):
    #     self.file.class_handler("test/test_relationship.txt")
    #     self.file.get_relationship("ClassE")
    #     actual = self.file.aggr_1_to_1
    #     expected = ["ClassF"]
    #     self.assertEqual(expected, actual, "cannot get 1 to 1 aggregation")
    #
    # def test_get_relationship_dependency(self):
    #     self.file.class_handler("test/test_relationship.txt")
    #     self.file.get_relationship("ToyBox")
    #     actual = self.file.dependency_list
    #     expected = ["Controller"]
    #     self.assertEqual(expected, actual, "cannot get dependency")
    #
    # def test_get_relationship_association(self):
    #     self.file.class_handler("test/test_relationship.txt")
    #     self.file.get_relationship("Controller")
    #     actual = self.file.association_list
    #     expected = ["Command"]
    #     self.assertEqual(expected, actual, "cannot get association")
