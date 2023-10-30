import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Plotting:
    def __init__(self, plot_option, x, data):
        self.plot_option = plot_option
        self.x = x
        self.data = data

    def plot(self):
        if self.plot_option == 1:
            return self.histogram()
        elif self.plot_option == 2:
            return self.boxplot()
        else:
            return "Invalid plot option"

    def histogram(self):
        self.data[self.x].hist()
        plt.title("Histogram of " + self.x)
        plt.show()
        return self.data[self.x].describe()

    def boxplot(self):
        self.data.boxplot(column=self.x)
        plt.title("Boxplot of " + self.x)
        plt.show()
        return self.data[self.x].describe()