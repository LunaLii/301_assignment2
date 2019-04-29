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
                    Controller.file.find_classes()
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

    def create_bar_chart(self):
        data = self.file.get_data()
        if self.file.get_data() == [0, 0, 0]:
            return False
        else:
            self.chart.create_bar_chart(data)

    def create_pie_chart(self):
        data = self.file.get_data()
        self.chart.create_pie_chart(data)

    def create_line_chart(self):
        data = self.file.get_data()
        self.chart.create_line_graph(data)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
