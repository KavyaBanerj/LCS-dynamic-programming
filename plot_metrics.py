#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:59:37 2023

@author: kavyabanerjee

Main Functions:
1. `read_metrics(filename)`: Reads LCS computation metrics from a specified file.
2. `plot_graph(metrics_list, output_graph_path)`: Plots and saves a graph showing LCS computation operations.
3. `plot_metrics(metrics_file, out_graph_file)`:  Calls modules for reading metrics and generating a plot.
4. `write_metrics(filename)`: Writes a list of LCS computation metrics to a CSV file.
5. `calculate_r_squared(observed, theoretical)`:  Calculates the R-squared value

Note:
This module visualizes LCS computation metrics, illustrating the variation in operations based on string lengths.
"""


import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.metrics import r2_score
from itertools import cycle

def read_metrics(filename):
    """
    Read the metrics from the provided filename.
    
    :param filename: Path object of the file to be read.
    :return: A list of dictionaries where each dictionary represents a row of metrics 
             with keys as the column names and values as the corresponding metric value.
    """
    metrics_list = []
    with open(filename, mode='r') as file:
        lines = file.readlines()
        if not lines:
            return metrics_list  
        
        header = lines[0].strip().split(",")  
        
        for line in lines[1:]:  # Skip  header
            cells = line.strip().split(",")  # split the line into cells
            row = {header[i]: cells[i] for i in range(len(header))}
            metrics_list.append(row)
    
    return metrics_list


def write_metrics(metrics_list, csv_output_graph_path):
    """
    Writes a list of LCS computation metrics to a CSV file.

    :param metrics_list: List of dictionaries where each dictionary contains 
                         the metrics for one pair of strings.
    :param csv_output_graph_path: Filename for the saved CSV with combined metrics.
    """
    # Assuming all dictionaries have the same keys, use the keys from the first dictionary for the header
    if not metrics_list:
        raise ValueError("The metrics list is empty, cannot write to CSV.")

    # Sort the metrics list by 'str1_len' (as integers)
    sorted_metrics = sorted(metrics_list, key=lambda x: int(x['str1_len']))
    
    # Get the keys from the first dictionary to use as the CSV column headers
    keys = sorted_metrics[0].keys()

    with open(csv_output_graph_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(sorted_metrics)


def calculate_r_squared(observed, theoretical):
    """
    Calculates the R-squared value comparing observed and theoretical data.

    :param observed: Array of observed values.
    :param theoretical: Array of theoretical values.
    :return: R-squared value.
    """
    return r2_score(observed, theoretical)

def plot_graph(metrics_list, output_graph_path, ):
    """
    Plots and saves a graph showing the number of operations for LCS computation, 
    grouped by the length of the first string in each pair. It also generates mirrored
    data points where str1_len and str2_len are swapped and saves the data used for
    plotting to a CSV file.

    :param metrics_list: List of dictionaries where each dictionary contains 
                         'str1_len', 'str2_len', and 'tot_ops' (total operations for LCS).
    :param output_graph_path: Filename for the saved plot.
    """
    plt.figure(figsize=(12, 7))

    # Group data by the length of the first string (m) and generate mirrored points
    grouped_operations = {}
    combined_metrics = []  # List to hold both original and mirrored metrics
    additional_metrics = [] 
    legend_handles = {}  # Dictionary to hold the legend handles
    
    
    # Define colors and markers to cycle through
    colors = cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange'])
    markers = {'observed': 'o', 'theoretical': 'x'}
    
    # Initialize R-squared values dictionary to store values for legend
    r_squared_values = {}

    # Process each entry and its mirrored entry
    for metrics in metrics_list:
        # Add original metrics to the combined list
        combined_metrics.append(metrics)
        
        # Original data point
        m, n = int(metrics['str1_len']), int(metrics['str2_len'])
        tot_ops = int(metrics['tot_ops'])
        grouped_operations.setdefault(m, {'n_values': [], 'operations_values': [], 'theoretical_values': []})
        grouped_operations[m]['n_values'].append(n)
        grouped_operations[m]['operations_values'].append(tot_ops)
        grouped_operations[m]['theoretical_values'].append(m * n)  # Theoretical efficiency

        # Mirrored data point
        # Skip adding mirrored point if m and n are the same, to avoid duplicating points
        if m != n:
            mirrored_metrics = metrics.copy()
            mirrored_metrics['str1_len'], mirrored_metrics['str2_len'] = mirrored_metrics['str2_len'], mirrored_metrics['str1_len']
            mirrored_metrics['pair_id'] = f'S{n}-S{m}'  # Update the pair_id for mirrored metrics
            combined_metrics.append(mirrored_metrics)  # Add mirrored metrics to the combined list

            grouped_operations.setdefault(n, {'n_values': [], 'operations_values': [], 'theoretical_values': []})
            grouped_operations[n]['n_values'].append(m)
            grouped_operations[n]['operations_values'].append(tot_ops)
            grouped_operations[n]['theoretical_values'].append(m * n)
            

    # Plot the data
    for m_len, data in grouped_operations.items():
        sorted_indices = np.argsort(data['n_values'])
        n_values = np.array(data['n_values'])[sorted_indices]
        operations_values = np.array(data['operations_values'])[sorted_indices]
        theoretical_values = np.array(data['theoretical_values'])[sorted_indices]
        
        # Calculate R-squared
        r_squared = calculate_r_squared(operations_values, theoretical_values)
        r_squared_values[m_len] = r_squared
        
        # Store additional metrics for CSV export
        for n_val, ops_val, theo_val in zip(n_values, operations_values, theoretical_values):
            additional_metrics.append({
                'str1_len': m_len,
                'str2_len': n_val,
                'tot_ops': ops_val,
                'theoretical_ops': theo_val,
                'r_squared': r_squared
            })
        
        color = next(colors)  # Get the next color from the cycle
        observed_marker = markers['observed']
        theoretical_marker = markers['theoretical']

        # Plot observed and theoretical with simplified legend
        plt.plot(n_values, operations_values, linestyle='-', color=color, marker=observed_marker)
        plt.plot(n_values, theoretical_values, linestyle='--', color=color, marker=theoretical_marker)
        
        # Add legend handles
        if m_len not in legend_handles:
            observed_handle = plt.Line2D([0], [0], color=color, marker=observed_marker, linestyle='-', label=f'(m = {m_len})')
            theoretical_handle = plt.Line2D([0], [0], color=color, marker=theoretical_marker, linestyle='--')
            legend_handles[m_len] = (observed_handle, theoretical_handle)
        
    plt.xlabel('Length of String Y (n)')
    plt.ylabel('Number of Operations')
    plt.title('LCS Operations: Observed vs. Theoretical Efficiency')
    
    # Add legend entries
    plt.legend(handles=[h[0] for h in legend_handles.values()])
    
    plt.grid(True)
    plt.savefig(output_graph_path, dpi=300)
    plt.show()

    # Save the combined metrics to a CSV file
    write_metrics(combined_metrics, 'metrics/combined_metrics.csv')
    # Save additional metrics to another CSV file
    write_metrics(additional_metrics, 'metrics/additional_metrics.csv')


def plot_metrics(metrics_file, out_graph_file):
    """
   Execute the entire plotting workflow
   
   :param metrics_file: The name of the file containing the metrics.
   :param out_graph_file: The name of the file where the plot will be saved.
   """   
    metrics_list = read_metrics(metrics_file)
    plot_graph(metrics_list, out_graph_file)
