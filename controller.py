from file_reader import FileReader
from chart_maker import ChartMaker
from os import path


class Controller:
    file = FileReader()
    chart = ChartMaker()

    @staticmethod
    def load_file(infile):
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
                self.file.output_file(file_location)
                print("created")
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("No such directory")
        except Exception as e:
            print(e)

    # def create_bar_chart(self):
    #     all_num = self.file.get_all_num()
    #     if all_num == [0, 0, 0]:
    #         return False
    #     else:
    #         self.chart.create_bar_chart(all_num)
    #
    # def create_pie_chart(self):
    #     all_num = self.file.get_all_num()
    #     self.chart.create_pie_chart(all_num)
    #
    # def create_line_chart(self):
    #     all_num = self.file.get_all_num()
    #     self.chart.create_line_graph(all_num)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
