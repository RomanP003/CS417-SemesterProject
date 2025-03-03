import sys

from parse_temps import parse_raw_temps

def main():

    input_temps = sys.argv[1]

    with open(input_temps, "r") as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file):
            print(temps_as_floats)

if __name__ == "__main__":
    main()