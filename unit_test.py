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

    def test_validate_attribute_name_true(self):
        self.assertTrue(self.validator.validate_attribute_name("attribute"))
        self.assertTrue(self.validator.validate_attribute_name("clement"))

    def test_validate_attribute_name_false(self):
        self.assertFalse(self.validator.validate_attribute_name("<clement"))
        self.assertFalse(self.validator.validate_attribute_name("??i"))
        self.assertFalse(self.validator.validate_attribute_name("break"))
        self.assertFalse(self.validator.validate_attribute_name("pass"))
        self.assertFalse(self.validator.validate_attribute_name(42))
        self.assertFalse(self.validator.validate_attribute_name(3.14))
        self.assertFalse(self.validator.validate_attribute_name(
            '--------------------------------------'
            '-------------------------------------'
        ))

    # Luna
    def test_validate_class_name_is_true(self):
        result_1 = self.validator.validate_class_name("Name")
        result_2 = self.validator.validate_class_name("ClassName")
        self.assertTrue(result_1, "invalid class name")
        self.assertTrue(result_2, "invalid class name")

    def test_validate_class_name_using_special_char(self):
        result = self.validator.validate_class_name("Name$%^&")
        self.assertFalse(result, "valid class name")

    def test_validate_class_name_using_lower(self):
        result = self.validator.validate_class_name("name")
        self.assertFalse(result, "valid class name")

    def test_validate_class_name_start_with_num(self):
        result = self.validator.validate_class_name("123Name")
        self.assertFalse(result, "valid class name")

    def test_validate_class_name_start_with_char(self):
        result = self.validator.validate_class_name("$%^_+Name")
        self.assertFalse(result, "valid class name")

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

    # Rajan
    def test_validate_method_name_is_false(self):
        validator = Validator()
        result_1 = validator.validate_method_name("Get")
        result_2 = validator.validate_method_name("1_get")
        result_3 = validator.validate_method_name("get_Name")
        self.assertFalse(result_1)
        self.assertFalse(result_2)
        self.assertFalse(result_3)

    def test_validate_method_name_is_true2(self):
        validator = Validator()
        result_1 = validator.validate_method_name("_get")
        result_2 = validator.validate_method_name("get1")
        self.assertTrue(result_1)
        self.assertTrue(result_2)

    def test_validate_method_name_is_true(self):
        validator = Validator()
        result_1 = validator.validate_method_name("method_name")
        result_2 = validator.validate_method_name("get")
        self.assertTrue(result_1)
        self.assertTrue(result_2)

    def test_validate_method_name_is_false2(self):
        validator = Validator()
        result_1 = validator.validate_method_name("Name")
        result_2 = validator.validate_method_name("get_Name")
        result_3 = validator.validate_method_name("1_get")
        self.assertFalse(result_1)
        self.assertFalse(result_2)
        self.assertFalse(result_3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
