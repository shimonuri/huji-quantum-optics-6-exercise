import numpy as np
import random
import matplotlib.pyplot as plt
import enum


class Result(enum.Enum):
    COINCIDENCE = 1
    LEFT_ONLY = 2
    RIGHT_ONLY = 3


def plot_g2_vs_rate():
    rates = np.linspace(0.1, 1.3 / 9.4e-9, 100)
    g2s = [get_g2(rate, 9.4e-9) for rate in rates]
    plt.plot(rates * 9.4e-9, g2s, label="Numeric")


def get_g2(rate, window, number_of_repetitions=10 ** 5):
    results = [make_experiment(rate, window) for _ in range(number_of_repetitions)]
    coincidences = results.count(Result.COINCIDENCE)
    left_only = results.count(Result.LEFT_ONLY) + coincidences
    right_only = results.count(Result.RIGHT_ONLY) + coincidences
    coincidence_chance = coincidences / number_of_repetitions
    left_only_chance = left_only / number_of_repetitions
    right_only_chance = right_only / number_of_repetitions
    return coincidence_chance / (left_only_chance * right_only_chance)


def make_experiment(rate, window):
    legs = get_legs(rate, window)
    if legs[0] != 0 and legs[1] != 0:
        return Result.COINCIDENCE
    elif legs[0] != 0:
        return Result.LEFT_ONLY
    elif legs[1] != 0:
        return Result.RIGHT_ONLY
    else:
        raise Exception("No legs")


def get_legs(rate, window):
    number_of_photons = 1 + np.random.poisson(rate * window)
    legs = [0, 0]
    for _ in range(number_of_photons):
        legs[random.randint(0, 1)] += 1
    return legs


if __name__ == "__main__":
    plot_g2_vs_rate()
