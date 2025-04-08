"""
This module is a function used that computes a line of best fit using least squares
approximation for the CPU temperatures project. This code may be used if it is imported
using ``from least_squares_approximation import {...} `` where ``{...}`` represents
one or more functions
"""
def least_squares_approximation(times, core_data, basename, coreNum):
    """
    Take two list containing times(x) and core temperature data(y), a file basename,
    and core number to compute a line for a set of times and core temperatures and
    appened the result to a file with a name made using the basename of the input file
    and the number of the core where the temperature readings are from.

    Args:
        times: times the temperature readings were taken

        core_data: temperature readings from a specific cpu core

        basename: input file name without the file extension

        coreNum: number of the CPU core the temperature readings are from(0-3)
    """
    if(len(times) != len(core_data)):
        raise ValueError("There should be an equal number of times and corresponding core temp readings.")

    sum_x_squared = 0
    sum_xy = 0

    k = len(times)

    sum_x = sum(times)

    for x in times:
        sum_x_squared += x**2

    sum_y = sum(core_data)

    for x, y in zip(times, core_data):
        sum_xy += x * y

    c1 = ((k * sum_xy) - (sum_x * sum_y)) / ((k * sum_x_squared) - pow(sum_x, 2))

    c0 = ((1/k) * (sum_y - (c1 * sum_x)))

    with open(f"{basename}-core-{coreNum}.txt", "a") as file:
        file.write(f"\t{times[0]:>4} <= x <= {times[-1]:>4} ; y ={c0:>11.4f} + {c1:>7.4f} x ; least-squares\n")