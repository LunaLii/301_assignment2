import unittest
from controller import Controller


class ControllerUnitTest(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_load_word_file(self):
        actual = self.controller.load_file("C:\\Users\Luna\PycharmProjects\\assignment2_refactoring\\test\\test2.docx")
        self.assertTrue(actual, "cannot load word file")

    def test_load_txt_file(self):
        actual = self.controller.load_file("C:\\Users\Luna\PycharmProjects\\assignment2_refactoring\\test\\test2.txt")
        self.assertTrue(actual, "cannot load txt file")

    def test_load_file_not_found_exception(self):
        actual = self.controller.load_file("C:\\Users\\Luna\\ICT\\test2.txt")
        self.assertRaises(FileNotFoundError, actual)

    def test_load_incorrect_file_exception(self):
        actual = self.controller.load_file("C:\\Users\Luna\PycharmProjects\\assignment2_refactoring\\test\\test2.csv")
        self.assertRaises(NameError, actual)

    # def test_get_correct_data_for_chart(self):
    #     self.controller.load_file("test/uml.txt")
    #     actual = len(self.controller.file.all_my_classes)
    #     expected = 2
    #     self.assertEqual(expected, actual, "cannot get the data")
