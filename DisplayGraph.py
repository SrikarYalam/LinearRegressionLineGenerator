''' Class to create and display various graphs during Gradient Descent
    Srikar Yalam
'''
import matplotlib.pyplot as plt
import numpy as np
from GradientDescent import *

class DisplayGraph:
    def __init__(self):
        pass

    def show_scatter_plot(self, x_values, y_values):
        plt.figure(1)
        plt.scatter(x_values, y_values, c = 'blue')
        plt.show()




