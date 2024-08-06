# Programming Project 3

This project aims to compare the performance of longest common subsequence problem (LCS) using dynamic programming.
The project counts individual cell comparisons to serve as a basis for comparison, and it handles alphanuermic strings.

### Python Specifications: 
1. IDE: Spyder IDE 5.4.3 (conda)
2. Python Version: Python 3.9.13 64-bit | Qt 5.15.2 | PyQt5 5.15.7 | Darwin 22.3.0 

## Files Description

#### 1. `lcs.py`
Implements LCS search using dynamic programming for 2 strings. Has functions to construct dp table and reconstruct LCS string.

#### 2. `read_input.py`
This module executes reading strings read from the file. It performs validation checks on input and contains functions to read and represent a string from a file.

#### 3. `write_output.py`
This module performs and writes the results of LCS pairs to an output file. It also writes runtime metrics to a CSV file.

#### 4. `plot_metrics.py`
This file creates visualizations for comparing the performance of LCS. Can be called optionally. 

## How To Run

1. Navigate to directory containing the README.md.
2. Run the program as a module: `python -m proj3 -h`. This will print the help message.
3. Run the program as a module (with real inputs): `python -m proj3 <input_file> <output_file>`
   a. IE: `python -m proj3 files/input/DynamicLab2Input.txt DynamicLab2Output.txt`

Output will be written to the specified output file after processing the input file.

### Note
- Please ensure that the input strings have only alphanumeric input.

### Usage

```commandline
usage: python -m proj3 [-h] [--plot] in_file out_file

positional arguments:
  in_file     Pathname of the input file.
  out_file    Pathname of the output file.

optional arguments:
  -h, --help      Show this help message and exit.
  --p, --plot      Include to plot the asymptotic analysis.

example:
python -m proj3 files/input/DynamicLab2Input.txt files/output/DynamicLab2Output.txt

# To plot runtime graph
python -m proj3 files/input/asymtoticInput.txt files/output/asymtoticOutput.txt -p
```
