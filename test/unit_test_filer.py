import unittest
from file_reader import FileReader


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

    def test_get_method_name(self):
        self.file.class_handler("test/uml.docx")
        self.file.find_classes()
        actual_one = []
        class_one = self.file.all_my_classes[0]
        for i in class_one.all_my_methods:
            actual_one.append(i.name)
        expected_one = ["add_toy", "get_toys"]
        class_two = self.file.all_my_classes[1]
        actual_two = []
        for i in class_two.all_my_methods:
            actual_two.append(i.name)
        expected_two = ["__str__"]
        self.assertEqual(expected_one, actual_one, "cannot get method name")
        self.assertEqual(expected_two, actual_two, "cannot get method name")

    def test_get_class_name(self):
        self.file.class_handler("test/uml.docx")
        self.file.find_classes()
        actual = []
        for x in self.file.all_my_classes:
            actual.append(x.name)
        expected = ["ToyBox", "Toy"]
        self.assertEqual(expected, actual, "cannot get class name")

    def test_get_attribute_name(self):
        self.file.class_handler("test/uml.docx")
        self.file.find_classes()
        actual_one = []
        class_one = self.file.all_my_classes[0]
        for i in class_one.all_my_attributes:
            actual_one.append(i.name)
        expected_one = ["number", "allMyToys"]
        class_two = self.file.all_my_classes[1]
        actual_two = []
        for i in class_two.all_my_attributes:
            actual_two.append(i.name)
        expected_two = ["name", "color", "price"]
        self.assertEqual(expected_one, actual_one, "cannot get attribute name")
        self.assertEqual(expected_two, actual_two, "cannot get attribute name")

    def test_get_relationship_one_composition(self):
        self.file.class_handler("test/test_relationship.txt")
        self.file.find_classes()
        class_two = self.file.all_my_classes[1]
        actual = []
        for i in class_two.all_my_relationships:
            i.identify_relationship_type()
            actual.append(i.compo_1_to_1)
        expected = [[], [], ['ClassB'], [], []]
        self.assertEqual(expected, actual, "cannot get 1 to 1 composition")

    def test_get_relationship_many_composition(self):
        self.file.class_handler("test/test_relationship.txt")
        self.file.find_classes()
        class_two = self.file.all_my_classes[1]
        actual = []
        for i in class_two.all_my_relationships:
            i.identify_relationship_type()
            actual.append(i.compo_1_to_many)
        expected = [[], ["Toy"], [], [], []]
        self.assertEqual(expected, actual, "cannot get 1 to many composition")

    def test_get_relationship_many_aggregation(self):
        self.file.class_handler("test/test_relationship.txt")
        self.file.find_classes()
        class_two = self.file.all_my_classes[1]
        actual = []
        for i in class_two.all_my_relationships:
            i.identify_relationship_type()
            actual.append(i.aggr_1_to_many)
        expected = [[], [], [], ['ClassD'], []]
        self.assertEqual(expected, actual, "cannot get 1 to many aggregation")

    def test_get_relationship_one_aggregation(self):
        self.file.class_handler("test/test_relationship.txt")
        self.file.find_classes()
        class_two = self.file.all_my_classes[1]
        actual = []
        for i in class_two.all_my_relationships:
            i.identify_relationship_type()
            actual.append(i.aggr_1_to_1)
        expected = [[], [], [], [], ['ClassF']]
        self.assertEqual(expected, actual, "cannot get 1 to 1 aggregation")

    def test_get_relationship_dependency(self):
        self.file.class_handler("test/test_relationship.txt")
        self.file.find_classes()
        class_two = self.file.all_my_classes[1]
        actual = []
        for i in class_two.all_my_relationships:
            i.identify_relationship_type()
            actual.append(i.dependency_list)
        expected = [["Controller"], [], [], [], []]
        self.assertEqual(expected, actual, "cannot get dependency")

    def test_get_relationship_association(self):
        self.file.class_handler("test/test_relationship.txt")
        self.file.find_classes()
        class_one = self.file.all_my_classes[0]
        actual = []
        for i in class_one.all_my_relationships:
            i.identify_relationship_type()
            actual.append(i.association_list)
        expected = [["Command"]]
        self.assertEqual(expected, actual, "cannot get association")

    def test_get_correct_data_for_chart(self):
        self.file.class_handler("test/uml.docx")
        self.file.find_classes()
        actual = self.file.get_data()
        expected = [2, 5, 3]
        self.assertEqual(expected, actual, "cannot get the data")
