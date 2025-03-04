import sys

from parse_temps import parse_raw_temps

def main():

    input_temps = sys.argv[1]

    """
        with open(input_temps, "r") as temps_file:
        # output raw structure
        for temps_as_floats in parse_raw_temps(temps_file):
            print(temps_as_floats)
    """

    with open(input_temps, "r") as temps_file:
        # split data

        times = []
        core_data = [[] for _ in range(0, 4)]

        for time, raw_core_data in parse_raw_temps(temps_file):
            times.append(time)
            for core_idx, reading in enumerate(raw_core_data):
                core_data[core_idx].append(reading)

        for time, *temps in list(zip(times, *core_data))[4:]:
            print(f"{time=} {temps=}")

if __name__ == "__main__":
    main()