from docx import Document
from validator import Validator
import os.path
from class_maker import ClassMaker


class FileReader:

    def __init__(self):
        self.all_my_classes = []
        self.relationship_list = []
        # self.class_name_list = []
        # self.num_all_attribute_list = []
        # self.num_all_method_list = []
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

    def get_data(self):
        class_num = len(self.all_my_classes)
        attribute_num = 0
        method_num = 0
        for x in self.all_my_classes:
            attribute_num += x.get_attribute_length()
            method_num += x.get_method_length()
        data = [class_num, attribute_num, method_num]
        return data

# c = FileReader()
# c.class_handler("test\\uml.txt")
# c.find_classes()
# c.get()
# c.output_file("C:\\Users\Luna\ICT\python_new\\")
    # Clement
    # def get_class_name(self, class_array):
    #     for listItem in class_array:
    #         if "class" in listItem:
    #             temp_class = listItem[:listItem.index(" {")]
    #             class_name = temp_class.split(' ')[1]
    #             return class_name

    # def get_attributes(self, class_array):
    #     attributes = []
    #     for listItem in class_array:
    #         if ":" in listItem and "(" not in listItem:
    #             result = listItem.split(' ')
    #             attributes.append(result[4])
    #     num_attribute = len(attributes)
    #     self.num_all_attribute_list.append(num_attribute)
    #     return attributes

    # def get_methods(self, class_array):
    #     methods = []
    #     for listItem in class_array:
    #         if "(" in listItem:
    #             methods.append(listItem[:listItem.index("\n")-2].strip())
    #     num_method = len(methods)
    #     self.num_all_method_list.append(num_method)
    #     return methods

    # Luna
    # def get_relationship(self, class_name):
    #     temp_relationship = []
    #     for a_relationship in self.relationship_list:
    #         r_class_name = a_relationship.split(" ")
    #         first_c_name = r_class_name[0]
    #         second_c_name = r_class_name[-1].replace("\n", "")
    #         if class_name == first_c_name:
    #             temp_relationship += self.identify_r_type(a_relationship,
    #                                                       second_c_name)
    #     return temp_relationship
    #
    # # Luna
    # def identify_r_type(self, a_relationship, name):
    #     a_r = ''
    #     if len(a_relationship.split(" ")) == 3:
    #         if "*--" in a_relationship:
    #             self.compo_1_to_1.append(name)
    #             a_r += "        # self. my_" + name.lower() + " -> " + name\
    #                 + "\n" + "        self." + name.lower() + " = " + "None \n"
    #         elif "o--" in a_relationship:
    #             self.aggr_1_to_1.append(name)
    #         elif "<--" in a_relationship:
    #             self.association_list.append(name)
    #         elif "<.." in a_relationship:
    #             self.dependency_list.append(name)
    #     else:
    #         if '"1" *-- "many"' in a_relationship:
    #             self.compo_1_to_many.append(name)
    #             a_r = "        # self. my_" + name.lower() + ": list" + " -> "\
    #                   + name + "\n" + "        self." + name.lower() + " = "\
    #                   + "None\n"
    #         elif '"1" o-- "many"' in a_relationship:
    #             self.aggr_1_to_many.append(name)
    #     return a_r
    #
    # def output_class(self, class_item):
    #     class_name = self.get_class_name(class_item)
    #     self.class_name_list.append(class_name)
    #     attribute_list = self.get_attributes(class_item)
    #     method_list = self.get_methods(class_item)
    #     relationship_list = self.get_relationship(class_name)
    #     result = "class " + class_name + ":\n    def __init__(self"
    #
    #     for listItem in attribute_list:
    #         result += ', ' + listItem
    #
    #     result += '):\n'
    #
    #     if Validator.validate_class_name(class_name):
    #         pass
    #
    #     for listItem in attribute_list:
    #         result += '        self.' + listItem + ' = ' + listItem + '\n'
    #         if Validator.validate_attribute_name(listItem):
    #             pass
    #
    #     if len(attribute_list) == 0:
    #         result += "        pass\n"
    #
    #     for list_item in relationship_list:
    #         result += list_item
    #
    #     for listItem in method_list:
    #         result += '\n'
    #         result += '    def ' + listItem + '(self):\n        # Todo: inco' \
    #                                           'mplete\n        pass\n'
    #     return result
    #
    # def output_classes(self, file_dir):
    #     files = []
    #     for classItem in self.class_list:
    #         files.append(file_dir + self.get_class_name(classItem) + '.py')
    #     for classItem, file in zip(self.class_list, files):
    #         if Validator.validate_class_name(self.get_class_name(classItem)):
    #             result = self.output_class(classItem)
    #             with open(file, "w") as output:
    #                 output.write(result)
    #     print("Files are created")
    #
    # def get_all_num(self):
    #     class_num = len(self.class_name_list)
    #     attribute_num = sum(self.num_all_attribute_list)
    #     method_num = sum(self.num_all_method_list)
    #     all_num = [class_num, attribute_num, method_num]
    #     return all_num


# c = FileReader()
# print(c.class_handler("test/uml.txt"))
