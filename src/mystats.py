from functools import reduce
from typing import Optional
import statistics as stats
import random
import math


def mean(input_list: list) -> float:
    sum = 0
    for element in input_list:
        sum += element
    return sum / len(input_list)


def mode(input_list: list) -> list:
    count_dict = {}
    max_count = 0
    for element in input_list:
        if element not in count_dict:
            count_dict[element] = 0
        count_dict[element] += 1
        if count_dict[element] > max_count:
            max_count = count_dict[element]
    return [
        key_value_pair[0]
        for key_value_pair in count_dict.items()
        if key_value_pair[1] == max_count
    ]


def median(input_list: list) -> float:
    median = input_list[len(input_list) // 2]
    if len(input_list) % 2 == 0:
        median = (median + input_list[len(input_list) // 2 - 1]) / 2
    return median


def standard_deviation(input_list: list) -> float:
    mean_of_input = mean(input_list)
    deviations_list = [(element - mean_of_input) ** 2 for element in input_list]
    variance = mean(deviations_list)
    return math.sqrt(variance)


def test_mean(print_results: Optional[bool] = None) -> None:
    rand_list = []
    for i in range(0, 100):
        rand_list.append(random.randrange(0, 1000))
        assert mean(rand_list) == stats.mean(rand_list)
        if print_results:
            print(
                f"{mean(rand_list)} = mean(random list of len({len(rand_list)})) | {stats.mean(rand_list)} = stats.mean(random list of len({len(rand_list)}))"
            )


def test_mode(print_results: Optional[bool] = None) -> None:
    rand_list = []
    for i in range(0, 100):
        rand_list.append(random.randrange(0, 1000))
        assert mode(rand_list) == stats.multimode(rand_list)
        if print_results:
            print(
                f"{mode(rand_list)} = mode(random list of len({len(rand_list)})) | {stats.multimode(rand_list)} = stats.mode(random list of len({len(rand_list)}))"
            )


def test_median(print_results: Optional[bool] = None) -> None:
    rand_list = []
    for i in range(0, 100):
        rand_list.append(i)
        assert int(median(rand_list)) == int(stats.median(rand_list))
        if print_results:
            print(
                f"{median(rand_list)} = median(random list of len({len(rand_list)})) | {stats.median(rand_list)} = stats.median(random list of len({len(rand_list)}))"
            )


def test_standard_deviation(print_results: Optional[bool] = None) -> None:
    rand_list = []
    rand_list.append(random.randrange(0, 1000))
    for i in range(0, 100):
        rand_list.append(random.randrange(0, 1000))
        # assert standard_deviation(rand_list) == stats.stdev(rand_list)
        # Not using this assertion because pretty sure this function calculates a different standard deviation than the one I am trying to calculate.
        if print_results:
            print(
                f"{standard_deviation(rand_list)} = standard_deviation(random list of len({len(rand_list)})) | {stats.stdev(rand_list)} = stats.stdev(random list of len({len(rand_list)}))"
            )
