from GradientDescent import *
from DisplayGraph import *
import numpy as np
import pandas as pd

def get_arrays_from_data():
    # csv to pandas dataframe
    df = pd.read_csv('example_data.csv', header =None)
    return df[0].to_numpy(), df[1].to_numpy


def main():
    # getting the data
    values = get_arrays_from_data()
    display = DisplayGraph()
    x_values = values[0]
    y_values = values[1]

    # displaying the scatter plot
    display.show_scatter_plot(x_values, y_values)

    # creating estimated w and b points with




if __name__ == '__main__':
    main()