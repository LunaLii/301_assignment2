from cmd import Cmd
from controller import Controller


class Command(Cmd):
    controller = Controller()

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>>"
        self.my_name = "unknown"

    # Luna
    def do_load(self, file):
        """
        Syntax: load [file]
        Load the PlantUML file that users want to convert into code frame
        :param file: a .txt or .docx file for PlantUML
        :return:
        """
        if self.controller.load_file(file):
            print("File is loaded")

    # Clement
    def do_create_class_files(self, file_dir):
        """
        Syntax: create_class_files [file_dir]
        Saves the file entered (either a .txt or docx file)
        :param file_dir: for the location of the file e.g. C:\\
        :return: none
        """
        self.controller.save_file(file_dir)

    # Rajan
    # Change commands and options: Luna: /a; Rajan: /p; Clement: /l
    def do_display(self, option):
        """
        Syntax: display [/a | /p | /l]
        Display bar chart, pie chart or line graph
        :param option: /a: display bar chart
                       /p: display pie chart
                       /l: display line graph
        :return: none
        """
        if option and option.strip():
            if option == "/a":
                if self.controller.create_bar_chart() is False:
                    print("Please load PlantUML and then create the class "
                          "files first")
                else:
                    self.controller.create_bar_chart()
            elif option == "/p":
                self.controller.create_pie_chart()
            elif option == "/l":
                self.controller.create_line_chart()
        else:
            print("please choose one")

    def do_quit(self, line):
        print("Quitting ......")
        return True


if __name__ == "__main__":
    command = Command()
    command.cmdloop()
