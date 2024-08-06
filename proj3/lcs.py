#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:57:41 2023

@author: kavyabanerjee

Main Functions:
1. `lcs_length(X, Y)`: Computes the length of the Longest Common Subsequence (LCS) between two strings X and Y.
2. `reconstruct_lcs(L, X, Y)`: Reconstructs the LCS from the computed matrix L, for strings X and Y.

Note:
This module is designed to calculate the LCS between pairs of strings.
 It includes functions for both computing the LCS length and reconstructing the LCS itself.
"""

def lcs_length(X, Y):
    """
    Calculates the length of the Longest Common Subsequence (LCS) between two strings.

    :param X: First string.
    :param Y: Second string.
    :return: Tuple containing the LCS matrix, total number of operations, and character comparisons.
    """
    # Get the lengths of the two strings
    m, n = len(X), len(Y)

    # Initialize a matrix for dynamic programming, filled with zeros
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Counters for operations and character comparisons
    total_operations, char_comparisons = 0, 0

    # Iterate over each character of the strings
    for i in range(m + 1):
        for j in range(n + 1):
            # Increment operation counter
            total_operations += 1

            # Fill the first row and first column with zeros (base case)
            if i == 0 or j == 0:
                L[i][j] = 0
            # When characters match, increment the value diagonally and add 1
            elif X[i - 1] == Y[j - 1]:
                char_comparisons += 1  # Increment character comparison counter
                L[i][j] = L[i - 1][j - 1] + 1
            # When characters do not match, take the max value from left or top cell
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Return the matrix, total operations, and character comparisons
    return L, total_operations, char_comparisons

def reconstruct_lcs(L, X, Y):
    """
    Reconstructs the Longest Common Subsequence (LCS) from the LCS matrix for strings X and Y.

    :param L: LCS matrix.
    :param X: First string.
    :param Y: Second string.
    :return: The LCS string.
    """
    # Initialize indices for iterating through the matrix
    i, j = len(X), len(Y)
    lcs_str = []  # List to store the LCS characters

    # Traverse the matrix from bottom-right to top-left
    while i > 0 and j > 0:
        # When the same character is found in both strings
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])  # Append the character to LCS
            i, j = i - 1, j - 1  # Move diagonally in the matrix
        # Move to the left or up in the matrix depending on the larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Return the LCS string by reversing the list and joining characters
    return ''.join(reversed(lcs_str))


# Example usage
# from read_input import read_input
# from itertools import combinations
# strings = read_input('/path/to/input/file.txt')
# for (name1, seq1), (name2, seq2) in combinations(strings.items(), 2):
#     L, total_ops, char_comps = lcs_length(seq1, seq2)
#     lcs_string = reconstruct_lcs(L, seq1, seq2)
#     print(f"LCS of '{name1}' and '{name2}' is '{lcs_string}' with {total_ops} total operations and {char_comps} character comparisons")
