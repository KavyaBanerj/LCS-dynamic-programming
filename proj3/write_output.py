#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:59:37 2023

@author: kavyabanerjee

Main Functions:
1. `write_output(filename, strings)`: Processes string pairs, calculates their LCS, writes the results, lengths, and runtime metrics to a specified file and a CSV file.

Helper Functions:
1. `calculate_lcs_for_pair(seq1, seq2)`: Calculates the LCS for a pair of sequences, along with additional statistics.
2. `write_runtime_metrics_to_csv(ilename, strings)`: Writes the runtime metrics to a CSV file.

Note:
This module exceuts LCS module and writes runtime metrics to an output file and a CSV file.
"""

from itertools import combinations
from proj3.lcs import lcs_length, reconstruct_lcs
import logging
import csv
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

def calculate_lcs_for_pair(seq1, seq2):
    """
    Calculates the LCS for a pair of sequences.

    :param seq1: First sequence.
    :param seq2: Second sequence.
    :return: Tuple containing LCS string, total operations, and character comparisons, other statistics
    """
    start_time = time.time()
    L, total_ops, char_comps = lcs_length(seq1, seq2)
    lcs_string = reconstruct_lcs(L, seq1, seq2)
    end_time = time.time()
    length_info = {
        'str_len1': len(seq1),
        'str_len2': len(seq2),
        'lcs_len': len(lcs_string)
    }
    
    return lcs_string, total_ops, char_comps, length_info, end_time - start_time

def write_runtime_metrics_to_csv(metrics_filename, metrics_list):
    """
    Writes runtime metrics of LCS calculations to a CSV file. The metrics include 
    pair identifier, lengths of the input strings, LCS length, total operations,
    character comparisons, and the runtime in seconds.
    
    :param metrics_filename: Name of the CSV file to write the metrics.
    :param metrics_list: List of metrics data to write to the CSV file.
    """
    with open(metrics_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['pair_id', 'str1_len', 'str2_len', 'lcs_len', 'tot_ops', 'char_comps', 'runtime'])
        writer.writerows(metrics_list)
        
        
        
def write_output(filename, strings):
    """
    Processes each pair of strings in both orders, calculates their LCS, and writes the results
    and metrics to the specified output file. It includes the lengths of the input strings
    and the LCS in the output. Outputs runtime metrics to CSV file.

    :param filename: String representing the name of the output file.
    :param strings: Dictionary of strings with keys as identifiers.
    """
    metrics_list = [] 

    with open(filename, "w") as file:
        
        logging.info("Processing strings in the file.")
        
        for (name1, seq1), (name2, seq2) in combinations(strings.items(), 2):
            # Process each combination in both directions
            for s1, n1, s2, n2 in [(seq1, name1, seq2, name2), (seq2, name2, seq1, name1)]:
                try:
                    # Perform lcs operations
                    lcs_string, total_ops, char_comps, length_info, runtime = calculate_lcs_for_pair(s1, s2)
                    # Append metrics data for CSV export
                    metrics_list.append((f"{n1}-{n2}", length_info['str_len1'], length_info['str_len2'], length_info['lcs_len'], total_ops, char_comps, runtime))

                    # Write the results and length information to the file
                    file.write(f"String 1: {n1} - {s1}\n")
                    file.write(f"String 1 Length: {length_info['str_len1']}\n")
                    file.write(f"String 2: {n2} - {s2}\n")
                    file.write(f"String 2 Length: {length_info['str_len2']}\n")
                    file.write(f"LCS: {lcs_string}\n")
                    file.write(f"LCS Length: {length_info['lcs_len']}\n")
                    file.write(f"Total operations: {total_ops}\n")
                    file.write(f"Character comparisons: {char_comps}\n")
                    file.write(f"Runtime: {runtime} seconds\n")
                    file.write("="*75 + "\n\n")

                    logging.info(f"Processed and wrote LCS for '{n1}' and '{n2}'.")

                except MemoryError:
                    logging.error("Error: Ran out of memory during LCS calculation for pair")
                    continue  # Skip to the next pair of strings
                
        # Call the function to write runtime metrics to a CSV file    
        logging.info("Writing to runtime metrics to runtime_metrics.csv")
        write_runtime_metrics_to_csv('metrics/runtime_metrics.csv', metrics_list)

        
# def write_output(filename, strings):
#     """
#     Processes each pair of strings, calculates their LCS, and writes the results
#     and metrics to the specified output file. It includes the lengths of the input strings
#     and the LCS in the output.
#     Outputs runtime metrics to CSV file

#     :param filename: String representing the name of the output file.
#     :param strings: Dictionary of strings with keys as identifiers.
#     """
#     metrics_list = [] 
    
#     with open(filename, "w") as file:
        
#         logging.info("Processing strings in the file.")
        
#         for (name1, seq1), (name2, seq2) in combinations(strings.items(), 2):
            
#             # Perform lcs operations
#             try:
#                 lcs_string, total_ops, char_comps, length_info, runtime = calculate_lcs_for_pair(seq1, seq2)
#                 # Append metrics data fot CSV export
#                 metrics_list.append((f"{name1}-{name2}", length_info['str_len1'], length_info['str_len2'], length_info['lcs_len'], total_ops, char_comps, runtime))
            
#             except MemoryError:
#                 logging.error("Error: Ran out of memory during LCS calculation for pair")
#                 continue  # Skip to the next pair of strings
                
#             # Write the results and length information to the file
#             file.write(f"String 1: {name1} - {seq1}\n")
#             file.write(f"String 1 Length: {length_info['str_len1']}\n")
#             file.write(f"String 2: {name2} - {seq2}\n")
#             file.write(f"String 2 Length: {length_info['str_len2']}\n")
#             file.write(f"LCS: {lcs_string}\n")
#             file.write(f"LCS Length: {length_info['lcs_len']}\n")
#             file.write(f"Total operations: {total_ops}\n")
#             file.write(f"Character comparisons: {char_comps}\n")
#             file.write(f"Runtime: {runtime} seconds\n")
#             file.write("="*75 + "\n\n")

#             logging.info(f"Processed and wrote LCS for '{name1}' and '{name2}'.")
            
#          # Call the function to write runtime metrics to a CSV file    
#         write_runtime_metrics_to_csv('runtime_metrics.csv', metrics_list)