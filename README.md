# CS417-SemesterProject

Repository for cs 417 semester project

# Requirements

    * Python 3.11+

# Execution and Output

usage: 
    python3 driver.py data/input_file.txt
    data/input_file.txt is used here because I moved my input files into a subdirectory

output similar to: 
    output files of the name {basename}-core-0.txt
    where {basename} is the name of the input file without the extension
    there will be numer of output files generated corresponding to the number of cores
    the files will consist of entries such as: 	   time1 <= x <=   time2 ; y =    constant_term + slope x ; interpolation
