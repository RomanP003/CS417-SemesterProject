"""
This module is a function used to computer a line for any pair of adjacent points
for the CPU Temperatures Project. This code may be used if it is imported using
``from piecewise_linear_itnerpolation import {...} ``where ``{...}`` represents
one or more functions.
"""

def piecewise_linear_interpolation(times, core_data, basename, coreNum):
    """
    Take two lists containing times and core temperature data, a file basename,
    and core number to compute a line for a pair of adjacent times and core temps
    and write the result to a file with a name made using the basename of the
    input file and number of the core where the temperature readings are from

    Args:
        times: times the temperature readings were taken

        core_data: temperature readings from a specific CPU core

        basename: input file name without the file extension

        coreNum: number of the CPU core the temperature readings are from(0-3)
    """
    
    if(len(times) != len(core_data)):
        raise ValueError("There should be an equal number of times and correspond core temp readings.")
    
    with open(f"{basename}-core-{coreNum}.txt", "w") as file:
        for i in range(1, len(core_data)):
            denominator = times[i] - times[i-1]

            numerator = core_data[i] - core_data[i-1]

            slope = numerator / denominator

            constant_term = core_data[i-1] - (slope * times[i-1])

            file.write(f"\t{times[i-1]:>4} <= x <= {times[i]:>4} ; y ={constant_term:>11.4f} + {slope:>7.4f} x ; interpolation\n")
