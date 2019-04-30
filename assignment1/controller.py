from fileHandler import PrintClass
from chart_maker import ChartMaker
from os import path


class Controller:
    file = PrintClass()
    chart = ChartMaker()

    @staticmethod
    def load_file(infile):
        r"""
        >>> Controller.load_file("C:\\Users\Luna\ICT\python\\uml.csv")
        Incorrect file type, please check with help load
        >>> Controller.load_file("test.docx")
        True
        >>> Controller.load_file("test.txt")
        True
        >>> Controller.load_file("C:\\Users\Luna\ICT\\uml.docx")
        File is not found
        """
        try:
            if path.isfile(infile):
                if ".txt" in infile[-4:] or ".docx" in infile[-5:]:
                    Controller.file.class_handler(infile)
                    return True
                else:
                    raise NameError

            else:
                raise FileNotFoundError

        except NameError:
            print("Incorrect file type, please check with help load")
        except FileNotFoundError:
            print("File is not found")
        except Exception as e:
            print(e)

    def save_file(self, file_location):
        try:
            if path.exists(file_location):
                self.file.output_classes(file_location)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("No such directory")
        except Exception as e:
            print(e)

    def create_bar_chart(self):
        all_num = self.file.get_all_num()
        if all_num == [0, 0, 0]:
            return False
        else:
            self.chart.create_bar_chart(all_num)

    def create_pie_chart(self):
        all_num = self.file.get_all_num()
        self.chart.create_pie_chart(all_num)

    def create_line_chart(self):
        all_num = self.file.get_all_num()
        self.chart.create_line_graph(all_num)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
