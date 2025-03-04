import sys

from parse_temps import parse_raw_temps
from piecewise_linear_interpolation import piecewise_linear_interpolation
def main():

    input_temps = sys.argv[1]

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

        for time, *temps in list(
            zip(times, core_0_data, core_1_data, core_2_data, core_3_data)
        ):
            print(f"{time=} {temps=}")

        piecewise_linear_interpolation(times, core_0_data)

if __name__ == "__main__":
    main()