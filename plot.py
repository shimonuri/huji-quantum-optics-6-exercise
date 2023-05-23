import pandas
import matplotlib.pyplot as plt


def plot_experimental_data(filename):
    data = pandas.read_csv("data/Exercise 6 Data.csv", names=["lamda", "coherence"])
    plt.plot(data)



