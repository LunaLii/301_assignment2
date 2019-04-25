from file_reader import PrintClass
import unittest
from validator import Validator
from controller import Controller


class TestDataExtraction(unittest.TestCase):
    # Clement
    def setUp(self):
        # be executed before each test
        self.test_class = PrintClass()
        self.validator = Validator()
        self.controller = Controller()

    def test_get_class_name(self):
        list_1 = ['class a {\n', '    n : String\n', '    add()\n', '}\n']
        list_2 = ['class  {\n', '    n : String\n', '    add()\n', '}\n']
        list_3 = ['    name : String\n', '    add_attributes()\n', '}\n']
        self.assertEqual(self.test_class.get_class_name(list_1), 'a')
        self.assertEqual(self.test_class.get_class_name(list_2), '')
        self.assertIsNone(self.test_class.get_class_name(list_3))

    def test_read_word_file(self):
        actual = self.test_class.read_word_file("test2.docx")
        expect = ["@startuml\n", "ToyBox *-- Toy\n", "\n", "class ToyBox {\n",
                  "    name : String\n", "}\n", "\n", "class Toy {\n", "}\n",
                  "@enduml\n"]
        self.assertEqual(expect, actual, "cannot read word file")

    def test_read_txt_file(self):
        actual = self.test_class.read_txt_file("test2.txt")
        expect = ["@startuml\n", "ToyBox *-- Toy\n", "\n", "class ToyBox {\n",
                  "    name : String\n", "}\n", "\n", "class Toy {\n", "}\n",
                  "@enduml\n"]
        self.assertEqual(expect, actual, "cannot read txt file")

    def test_load_word_file(self):
        actual = self.controller.load_file("test2.docx")
        self.assertTrue(actual, "cannot load word file")

    def test_load_txt_file(self):
        actual = self.controller.load_file("test2.txt")
        self.assertTrue(actual, "cannot load txt file")

    def test_load_file_not_found_exception(self):
        actual = self.controller.load_file("C:\\Users\\Luna\\ICT\\test2.txt")
        self.assertRaises(FileNotFoundError, actual)

    def test_load_incorrect_file_exception(self):
        actual = self.controller.load_file("test2.csv")
        self.assertRaises(NameError, actual)

    def test_get_method_name(self):
        class_item = self.test_class.class_handler("test_method.docx")
        actual_one = self.test_class.get_methods(class_item[0])
        expected_one = ["add_toy", "get_toy"]
        actual_two = self.test_class.get_methods(class_item[1])
        expected_two = ["__str__"]
        self.assertEqual(expected_one, actual_one, "cannot get method name")
        self.assertEqual(expected_two, actual_two, "cannot get method name")


if __name__ == '__main__':
    unittest.main(verbosity=2)
