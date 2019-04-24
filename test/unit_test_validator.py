import unittest
from validator import Validator

class ValidatorUnitTest(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

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

    def test_validate_attribute_name_is_true(self):
        result = self.validator.validate_attribute_name("attribute")
        self.assertTrue(result, "invalid attribute name")

    def test_validate_attribute_name_is_false(self):
        result = self.validator.validate_attribute_name("pass")
        self.assertFalse(result, "valid attribute name")

    def test_validate_attribute_name_is_false_2(self):
        result = self.validator.validate_attribute_name("!?abc")
        self.assertFalse(result, "valid attribute name")

    def test_validate_method_name_is_true(self):
        result = self.validator.validate_method_name("test")
        self.assertTrue(result, "invalid method name")

    def test_validate_method_name_is_false(self):
        result = self.validator.validate_method_name("1test")
        self.assertFalse(result, "valid method name")

    def test_validate_method_name_is_false_2(self):
        result = self.validator.validate_method_name("!$test")
        self.assertFalse(result, "valid method name")

if __name__ == '__main__':
    unittest.main(verbosity=2)