#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 22:33:09 2023

@author: kavyabanerjee

Main Functions:
1. `read_input(filename)`: Reads strings from a file and returns them as a dictionary. Logs an error message and returns None if an exception occurs.

Helper Functions:
1. `read_strings(file)`: Reads a series of strings from a file object and returns them as a dictionary.
2. `is_valid_string(line)`: Checks if a line contains a valid string format.

Note:
This module is responsible for reading and validating strings from a specified file. 
It includes error handling and logging.
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# def is_valid_string(line):
#     """
#     Checks if a line contains a valid string in the format 'key=value'.
#     Both key and value must be non-empty alphanumeric strings.

#     :param line: String line.
#     :return: True if valid; False otherwise.
#     """
#     parts = line.split('=', 1)
#     if len(parts) != 2 or not parts[0].strip() or not parts[1].strip():
#         return False
#     return parts[0].strip().isalnum() and parts[1].strip().isalnum()

# def read_strings(file):
#     """
#     Reads a series of strings from a file object. Validates each line and stops processing
#     if a duplicate key is found or skips invalid entries.

#     :param file: File object pointing to the input file.
#     :return: Dictionary of validated strings.
#     :raises ValueError: If a duplicate key is found.
#     """
#     strings = {}
#     for line_number, line in enumerate(file, start=1):
#         if is_valid_string(line):
#             key, value = line.split('=', 1)
#             key = key.strip()
#             if key in strings:
#                 raise ValueError(f"Duplicate key '{key}' found at line {line_number}. Stopping processing.")
#             strings[key] = value.strip()
#         else:
#             logging.warning(f"Skipping invalid line {line_number}: '{line.strip()}'.")
#     return strings


def is_valid_string(line):
    """
    Checks if a line contains a valid string in the format 'key=value'.
    Both key and value must be non-empty alphanumeric strings.

    :param line: String line.
    :return: Tuple of (bool, str), where bool indicates if the line is valid,
             and str contains an error message if it's not valid.
    """
    parts = line.split('=', 1)
    if len(parts) != 2:
        return False, "Line must contain a key and a value separated by '='."
    key, value = parts
    if not key.strip():
        return False, "Key part is missing."
    if not value.strip():
        return False, "Value part is missing."
    if not (key.strip().isalnum() and value.strip().isalnum()):
        return False, "Both key and value must be alphanumeric."
    return True, ""

def read_strings(file):
    """
    Reads a series of strings from a file object, validates each line,
    and stops processing if a duplicate key is found.

    :param file: File object pointing to the input file.
    :return: Dictionary of validated strings.
    :raises ValueError: If a duplicate key is found.
    """
    strings = {}
    for line_number, line in enumerate(file, start=1):
        is_valid, error_msg = is_valid_string(line)
        if not is_valid:
            logging.warning(f"Skipping invalid line {line_number}: {error_msg}")
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        if key in strings:
            raise ValueError(f"Duplicate key '{key}' found at line {line_number}. Stopping processing.")
        strings[key] = value.strip()
        
    if len(strings) < 2:
        raise ValueError("At least two valid strings are required. Insufficient valid data.")

    return strings


def read_input(filename):
    """
    Reads strings from the specified file and returns them in a dictionary.
    Handles file reading errors and logs appropriate messages.

    :param filename: Path of the input file.
    :return: Dictionary of strings read from the file, or None if an error occurs.
    """
    try:
        with open(filename, "r") as file:
            return read_strings(file)
    except Exception as e:
        logging.error(f"Error reading '{filename}': {e}")
        return None
