import matplotlib.pyplot as plt
from file_reader import FileReader


class ChartMaker:
    # Luna
    file_reader = FileReader()

    def create_bar_chart(self, data):
        name_list = ["Class", "Attribute", "Method"]
        numbers = data
        size = range(len(numbers))
        plt.bar(size, numbers, tick_label=name_list)
        plt.ylabel("Number")
        plt.xlabel("Elements of UML")
        plt.title("The total counts for three elements of the UML")
        plt.show()

    # Rajan
    def create_pie_chart(self, data):
        plt.figure(figsize=(5, 5))
        labels = ["Total number of ClassNum", "Total number of AttributeNum",
                  "Total number of MethodNum"]
        values = data
        explode = [0, 0.05, 0]
        plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode)
        plt.title("Number of Classes, Attributes and Methods\n")
        plt.legend(labels, loc=3)
        plt.show()

    # Clement
    def create_line_graph(self, data):
        plt.title('Number of Classes, Attributes and Methods')
        plt.xlabel('1: Classes, 2: Attributes, 3: Methods')
        plt.ylabel('Total counts for each: (classes, attributes, methods)')
        x = [1, 2, 3]
        y = data
        plt.plot(x, y)
        plt.show()
