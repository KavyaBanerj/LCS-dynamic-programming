#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:26:22 2023

@author: kavyabanerjee

Main driver program
This script is used to read input data from a file, perform validations,
and perform lcs operations and output statistics.
Wite the output lcs and statistics to a file. Also creates a runtime metrics csv.

The script also checks for input errors and can be run with optional flags 
for plotting asymptotic analysis.

"""

import argparse
from pathlib import Path
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Import the read_input, write_output and plot_metrics functions 
from proj3.read_input import read_input
from proj3.write_output import write_output
from proj3.plot_metrics import plot_metrics

def check_io_errors(in_path, out_path):
    """
    Check the existence and validity of the input file and the output directory.
    
    :param in_path: Path object representing the input file path.
    :param out_path: Path object representing the output file path.
    """
    
    # Check if input file exists
    if not in_path.exists() or not in_path.is_file():
        sys.stderr.write(f"Error: Input file {in_path} does not exist or is not a file.\n")
        sys.exit(1)

    # Check if output directory exists, if not create one
    if not out_path.parent.exists():
        logging.info(f"Output directory {out_path.parent} does not exist.\nCreating output directory.")
        try:
            out_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            sys.stderr.write(f"Error: Cannot create output directory {out_path.parent}. {str(e)}\n")
            sys.exit(1)

def main():
    """
    Main function to parse arguments, read input strings, and write output to file.
    """
    # Create the parser
    parser = argparse.ArgumentParser()
    
    #  Define mandatory arguments
    parser.add_argument("in_file", type=str, help="Pathname of the input file")
    parser.add_argument("out_file", type=str,  help="Pathname of the output file")
    
    # Define optional arguments, plot flag:
    parser.add_argument("--plot", "-p", action="store_true", help="Include to plot the asymptotic analysis")
    
    # Parse the arguments
    args = parser.parse_args()
    in_path = Path(args.in_file)
    out_path = Path(args.out_file)
    
    try:
        check_io_errors(in_path, out_path)
        
        # Read strings from the input file
        strings = read_input(in_path)
        
        if not strings:
            sys.exit("Error: No valid strings found in the input file.")
            
           
        # Writestringsto the output file
        write_output(args.out_file, strings)
        
        # print a completion message to the console
        print(f"Processing complete. Output written to {out_path}.")
        
        # If plot is set, plot runtime metrics
        if args.plot:
            metrics_folder = Path("metrics")
            #  check existence of the 'metrics' directory, create if not exist
            if not metrics_folder.exists():
                logging.info("'metrics' folder does not exist.\nCreating 'metrics' folder.")
                try:
                    metrics_folder.mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    sys.stderr.write(f"Error: Cannot create 'metrics' directory. {str(e)}\n")
                    sys.exit(1)
            
            logging.info("Plotting runtime metric graph.")
            plot_metrics(metrics_folder / "runtime_metrics.csv", metrics_folder / "runtime_metrics.png")

    except (FileNotFoundError, PermissionError, ValueError) as e:
        sys.stderr.write(f"Error: {e}\nExiting program")
        sys.exit(1)


if __name__ == "__main__":
    main()
