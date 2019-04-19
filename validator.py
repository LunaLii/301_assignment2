from re import match
from re import compile


class Validator:
    # Luna
    @staticmethod
    def validate_class_name(class_name):
        """
        >>> Validator.validate_class_name("ClassBuilder")
        True
        >>> Validator.validate_class_name("ClassName123")
        True
        >>> Validator.validate_class_name("classBuilder")
        False
        >>> Validator.validate_class_name("C!#Name")
        False
        >>> Validator.validate_class_name("ClassName>")
        False
        >>> Validator.validate_class_name("1ClassName>")
        False
        >>> Validator.validate_class_name("-+ClassName>")
        False
        """
        if class_name[0].isupper() and match("^[A-Za-z0-9]*$", class_name):
            return True
        return False

    @staticmethod
    def validate_attribute_name(name):
        """
        >>> Validator.validate_attribute_name("Name")
        False
        >>> Validator.validate_attribute_name("break")
        False
        >>> Validator.validate_attribute_name("a")
        False
        >>> Validator.validate_attribute_name(1234)
        False
        >>> Validator.validate_attribute_name("attribute")
        True
        >>> Validator.validate_attribute_name("Sometimes" \
                "python programming can be hard")
        False
        >>> Validator.validate_attribute_name("/&*(")
        False
        """

        # below is doctest

        regex = compile('[@!#$%^&*()<>?/|}{~:A-Z]')
        res = [
            'and',
            'assert',
            'break',
            'class',
            'continue',
            'def',
            'del',
            'elif',
            'else',
            'except',
            'exec',
            'finally',
            'for',
            'from',
            'global',
            'if',
            'import',
            'in',
            'is',
            'lambda',
            'not',
            'or',
            'pass',
            'print',
            'raise',
            'return',
            'try',
            'while',
        ]
        if not isinstance(name, str) or name in res or \
                not 1 < len(name) < 31 or regex.search(name) is not None:
            return False
        else:
            return True

    # Rajan

    @staticmethod
    def validate_method_name(name):
        """
        >>> Validator.validate_method_name("Name")
        False
        >>> Validator.validate_method_name("method_name")
        True
        >>> Validator.validate_method_name("get_A")
        False
        >>> Validator.validate_method_name("get")
        True
        >>> Validator.validate_method_name("_get")
        True
        >>> Validator.validate_method_name("1_get")
        False
        >>> Validator.validate_method_name("get1")
        True
        """

        # below is doctest

        regex = compile('[@!#$%^&*()<>?/|}{~:A-Z]')
        if regex.search(name) is not None or name[0].isdigit():
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
