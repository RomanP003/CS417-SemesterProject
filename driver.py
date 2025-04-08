import sys

from parse_temps import parse_raw_temps
from piecewise_linear_interpolation import piecewise_linear_interpolation
from least_squares_approximation import least_squares_approximation

def main():

    input_temps = sys.argv[1]
    
    no_extension = sys.argv[1].replace(".txt", "")
    basename = no_extension.replace("data/", "")
    print(basename)

    with open(input_temps, "r") as temps_file:
        # ----------------------------------------------------------------------
        # Split Data
        # ----------------------------------------------------------------------
        times = []
        core_0_data = []
        core_1_data = []
        core_2_data = []
        core_3_data = []
        for time, core_data in parse_raw_temps(temps_file):
            times.append(time)
            core_0_data.append(core_data[0])
            core_1_data.append(core_data[1])
            core_2_data.append(core_data[2])
            core_3_data.append(core_data[3])

        piecewise_linear_interpolation(times, core_0_data, basename, 0)
        least_squares_approximation(times, core_0_data, basename, 0)
        piecewise_linear_interpolation(times, core_1_data, basename, 1)
        least_squares_approximation(times,core_1_data, basename, 1)
        piecewise_linear_interpolation(times, core_2_data, basename, 2)
        least_squares_approximation(times,core_2_data, basename, 2)
        piecewise_linear_interpolation(times, core_3_data, basename, 3)
        least_squares_approximation(times,core_3_data, basename, 3)

if __name__ == "__main__":
    main()