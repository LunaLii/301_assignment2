from docx import Document
from validator import Validator
import os.path
from class_maker import ClassMaker


class FileReader:

    def __init__(self):
        self.all_my_classes = []
        self.relationship_list = []
        self.class_list = []

    # Luna: load data from .docx file
    # Clement: exception
    def read_word_file(self, file_name):
        try:
            if os.path.isfile(file_name):
                file = Document(file_name)
                content = []
                for para in file.paragraphs:
                    content.append(para.text + "\n")
                return content
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            raise FileNotFoundError("Cannot find this file")
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

    # Clement: load data from .txt file
    # Rajan: exception
    def read_txt_file(self, file_name):
        try:
            if os.path.isfile(file_name):
                file = open(file_name, 'r').readlines()
                return file
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            raise FileNotFoundError("File doesn't exist")
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

    def class_handler(self, file_name):
        class_list = [[]]
        file_content = []
        if ".txt" in file_name[-4:]:
            file_content = self.read_txt_file(file_name)
        elif ".docx" in file_name[-5:]:
            file_content = self.read_word_file(file_name)
        for i, m in enumerate(file_content[1:-1]):
            if m == "\n":
                if i != len(file_content[1:-1]) - 1:
                    class_list.append([])
            else:
                class_list[-1].append(m)
        self.relationship_list = class_list[0]
        self.class_list = class_list[1:]
        return self.class_list

    def find_classes(self):
        for a_class in self.class_list:
            class_name = ""
            relationships = []
            attributes = []
            methods = []
            for item in a_class:
                if "class" in item:
                    temp_class = item[:item.index(" {")]
                    class_name = temp_class.split(' ')[1]
                if ":" in item and "(" not in item:
                    attributes.append(item)
                if "(" in item:
                    methods.append(item)
            for a_relationship in self.relationship_list:
                if a_relationship.find(class_name) != -1:
                    relationships.append(a_relationship)
            self.add_class(class_name, attributes, methods, relationships)

    def add_class(self, class_name, attributes, methods, relationships):
        new_class = ClassMaker(class_name, attributes, methods, relationships)
        new_class.add_class_attributes()
        new_class.add_class_methods()
        new_class.add_class_relationships()
        self.all_my_classes.append(new_class)

    def output_file(self, file):
        for x in self.all_my_classes:
            if Validator.validate_class_name(x.name):
                file_name = file + x.name + ".py"
                with open(file_name, "w") as output:
                    output.write(x.print_class())
