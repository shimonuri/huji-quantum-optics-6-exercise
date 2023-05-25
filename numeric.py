import numpy as np
import random
import matplotlib.pyplot as plt
import enum


class Result(enum.Enum):
    COINCIDENCE = 1
    LEFT_ONLY = 2
    RIGHT_ONLY = 3


class Method(enum.Enum):
    PROBABILITIES = 1
    COUNT = 2


def plot_g2_vs_rate(method):
    rates = np.linspace(0.1, 1.3 / 9.4e-9, 100)
    g2s = [get_g2(rate, 9.4e-9, method=method) for rate in rates]
    plt.plot(rates * 9.4e-9, g2s, label="Numeric")


def get_g2(
    rate,
    window,
    number_of_repetitions=10**5,
    method=Method.PROBABILITIES,
):
    results = [make_experiment(rate, window, method) for _ in range(number_of_repetitions)]
    if method == Method.PROBABILITIES:
        coincidences = results.count(Result.COINCIDENCE)
        left_only = results.count(Result.LEFT_ONLY) + coincidences
        right_only = results.count(Result.RIGHT_ONLY) + coincidences
        coincidence_chance = coincidences / number_of_repetitions
        left_only_chance = left_only / number_of_repetitions
        right_only_chance = right_only / number_of_repetitions
        return coincidence_chance / (left_only_chance * right_only_chance)
    elif method == Method.COUNT:
        coincidence = np.mean([result[0] * result[1] for result in results])
        left_only = np.mean([result[0] for result in results])
        right_only = np.mean([result[1] for result in results])
        return coincidence / (left_only * right_only)
    else:
        raise Exception("Invalid method")


def make_experiment(rate, window, method=Method.PROBABILITIES):
    legs = get_legs(rate, window)
    if method == Method.PROBABILITIES:
        if legs[0] != 0 and legs[1] != 0:
            return Result.COINCIDENCE
        elif legs[0] != 0:
            return Result.LEFT_ONLY
        elif legs[1] != 0:
            return Result.RIGHT_ONLY
        else:
            raise Exception("No legs")
    elif method == Method.COUNT:
        return legs
    else:
        raise Exception("Invalid method")


def get_legs(rate, window):
    number_of_photons = 1 + np.random.poisson(rate * window)
    legs = [0, 0]
    for _ in range(number_of_photons):
        legs[random.randint(0, 1)] += 1
    return legs


if __name__ == "__main__":
    plot_g2_vs_rate(method=Method.COUNT)
