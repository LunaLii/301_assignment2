from re import match
from re import compile


class Validator:
    @staticmethod
    def validate_class_name(class_name):
        if class_name[0].isupper() and match("^[A-Za-z0-9]*$", class_name):
            return True
        return False

    @staticmethod
    def validate_attribute_name(name):
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

    @staticmethod
    def validate_method_name(name):
        regex = compile('[@!#$%^&*()<>?/|}{~:A-Z]')
        if regex.search(name) is not None or name[0].isdigit():
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
