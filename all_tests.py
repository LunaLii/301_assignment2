import doctest
import unittest
from test.unit_test_validator import ValidatorUnitTest


def doc_test():
    pass


def unit_test():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(ValidatorUnitTest))

    return the_suite


if __name__ == "__main__":
    doc_test()
    runner = unittest.TextTestRunner(verbosity=2)

    test_suite = unit_test()
    runner.run(test_suite)
