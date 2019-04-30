import matplotlib.pyplot as plt


class ChartMaker:
    # Luna
    def create_bar_chart(self, all_num):
        name_list = ["Class", "Attribute", "Method"]
        numbers = all_num
        size = range(len(numbers))
        plt.bar(size, numbers, tick_label=name_list)
        plt.ylabel("Number")
        plt.xlabel("Elements of UML")
        plt.title("The total counts for three elements of the UML")
        plt.show()

    # Rajan
    def create_pie_chart(self, all_num):
        plt.figure(figsize=(5, 5))
        labels = ["Total number of ClassNum", "Total number of AttributeNum",
                  "Total number of MethodNum"]
        values = all_num
        explode = [0, 0.05, 0]
        plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode)
        plt.title("Number of Classes, Attributes and Methods\n")
        plt.legend(labels, loc=3)
        plt.show()

    # Clement
    def create_line_graph(self, all_num):
        plt.title('Number of Classes, Attributes and Methods')
        plt.xlabel('1: Classes, 2: Attributes, 3: Methods')
        plt.ylabel('Total counts for each: (classes, attributes, methods)')
        x = [1, 2, 3]
        y = all_num
        plt.plot(x, y)
        plt.show()
