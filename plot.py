import numpy as np
import pandas
import matplotlib.pyplot as plt

import numeric


plt.rcParams.update({"font.size": 22})


def plot_experimental_data(filename):
    data = pandas.read_csv(filename, names=["lamda", "coherence"])
    data.sort_values(by=["lamda"], inplace=True)
    plt.plot(data["lamda"], data["coherence"], "o", label="Experimental Data")
    plt.xlabel(r"$Nw$")
    plt.ylabel("$g^{(2)}(0)$")


def plot_theoretical_data():
    theoretical_g = lambda x: (x * (x + 2)) / ((1 + x) ** 2)
    x = np.linspace(0, 1.3, 100)
    y = [theoretical_g(i) for i in x]
    plt.plot(x, y, label="Theoretical ($Nw(Nw+2)/(1+Nw)^2$))")


if __name__ == "__main__":
    plot_experimental_data("data/Exercise 6 Data.csv")
    plot_theoretical_data()
    numeric.plot_g2_vs_rate()
    plt.legend()
    plt.show()
