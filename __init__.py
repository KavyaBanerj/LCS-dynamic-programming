#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:13:37 2023

@author: kavyabanerjee

Package for LCS search using dynamic programming and utilities.

Modules:
 1. `lcs.py`
Implements LCS search using dynamic programming for 2 strings. Has functions to construct dp table and reconstruct LCS string.

 2. `read_input.py`
This module executes reading strings read from the file. It performs validation checks on input and contains functions to read and represent a string from a file.

 3. `write_output.py`
This module performs and writes the results of LCS pairs to an output file. It also writes runtime metrics to a CSV file.

 4. `plot_metrics.py`
This file creates visualizations for comparing the performance of LCS. Can be called optionally.
"""
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

