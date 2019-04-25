import unittest
from test.unit_test_validator import ValidatorUnitTest
from test.unit_test_filer import FilerUnitTest


def doc_test():
    import doctest
    doctest.testfile("test/doc_test_validator.txt", verbose=1)
    # doctest.testfile("doc_test_validator.txt", verbose=1)

def unit_test():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(ValidatorUnitTest))
    the_suite.addTest(unittest.makeSuite(FilerUnitTest))
    return the_suite


if __name__ == "__main__":
    doc_test()
    runner = unittest.TextTestRunner(verbosity=2)

    test_suite = unit_test()
    runner.run(test_suite)
