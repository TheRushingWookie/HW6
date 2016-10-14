################################################################################
#
#   HW6
#   Due Wednesday October 19, 11:59pm
#
################################################################################


# Sorted Matrix Search
#
# Write a function that, given a square 2d array (matrix) of integers and a
# target integer, will return the 'coordinates' of the target integer as a
# tuple in the form (row, col) if the element exists in the matrix, or (-1, -1)
# if the element does not exists.
#
# The matrix is guaranteed to be sorted ascending row-wise, and the zeroth
# element of each row is strictly larger than the last element of the
# previous row.
#
# Your solution should run in O(logn) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: [[1,2,3],[8,11,16],[23,24,25]], 8
#   Output:
#   (1, 0)
#
# Example 2:
#   Input: [[1,2,3],[8,11,16],[23,24,25]], 20
#   Output:
#   (-1, -1)
#
# Parameters
# ----------
# matrix : List[List[int]]
#   A square 2d array of integers
#
# target : int
#   The target integer to search the matrix for
#
# Returns
# -------
# Tuple(int, int)
#   Returns (row, col) coordinates of the target, or (-1, -1) if the target
#   is not in the matrix
#
def sorted_matrix_search(matrix, target):
    pass

# Array Almost Product
#
# Write a function that, given a list of integers, will return a list of
# integers 'output' wherein the value of output[i] is the product of all the
# numbers in the input array except for input[i].
#
# Note: Your solution *cannot* use division in any way.
#
# Your solution should run in O(n) time. Your solution should not allocate
# any space other than the output list.
#
# Example(s)
# ----------
# Example 1:
#   Input: [2,3,4,5]
#       Output should be [3*4*5, 2*4*5, 2*3*4]
#   Output: [60, 40, 30, 24]
#
# Example 2:
#   Input: [3,6,9,-3,2,-2]
#   Output:
#   [648, 324, 216, -648, 972, -972]
#
# Parameters
# ----------
# arr : List[int]
#   A list of integers. You can assume len(arr) > 1
#
# Returns
# -------
# List[int]
#   Returns a list where every element of the list is the product of
#   all the numbers in the input list except for the number at the index
#   being evaluated.
#
def array_almost_product(arr):
    pass

# Pascal's Triangle
#
# Write a function that, given an index i, returns the i'th row of Pascal's
# Triangle.
#
# This Wikipedia page on Pascal's triangle may be useful:
#   https://en.wikipedia.org/wiki/Pascal%27s_triangle
#
# Your solution should run in O(i) time and use O(i) space.
#
# Example(s)
# ----------
# Example 1:
#   Input: 2
#   Output: [1,2,1]
#
# Example 2:
#   Input: 6
#   Output: [1,6,15,20,15,6,1]
#
# Parameters
# ----------
# i : int
#   The row index of the row of Pascal's Triangle you are searching for
#
# Returns
# -------
# List[int]
#   Returns the i'th row of Pascal's Triangle as a list of ints
#
def pascals_triangle(i):
    pass

# Alive People
#
# Write a function that, given a list of strings representing a person's birth year and their final age,
# will return the year that had the most people alive (inclusive). If there are multiple years that tie, return the earliest.
#
# Examples
# ----------
# Example 1:
#   Input: ["1920: 80", "1940: 22", "1961: 10"]
#   Output: 1961
#
# Example 2:
#   Input: ["2000: 46", "1990: 17", "1200: 97", "1995: 20"]
#   Output: 2000
#
# Parameters
# ----------
# people : List[string]
#   A list of strings each representing a birth year and final age
#
#
# Returns
# -------
# int
#   Returns earliest year with the most people alive
#
def alive_people(people):
    pass

# Number to Text
#
# Write a function that given a number from 0-100, will return the string which is a English representation of the number.
# The result should be lower case and spaced out with no dashes
#
# Your solution should run in O(n) time. Your solution should not allocate
# any space other than the output list.
#
# Example(s)
# ----------
# Example 1:
#   Input: 100
#   Output: one hundred
#
# Example 2:
#   Input: 74
#   Output:
#   seventy four
#
# Example 3:
#   Input: 19
#   Output:
#   nineteen
#
# Example 4:
#   Input: 28
#   Output:
#   twenty eight
#
# Parameters
# ----------
# number : int
#   A number from 0-100
#
# Returns
# -------
# string
#   English representation of the number
#
def number_to_text(number):
    pass

# Rotate Matrix
#
# Write a function that given an NxN matrix will rotate the matrix to the left 90 degrees
#
# Examples
# ----------
# Example 1:
#   Input: [[1,2],[3,4]]
#   Output: [[2,4],[1,3]]
#
# Example 2:
#   Input: [[1,2,3],[4,5,6],[7,8,9]]
#   Output: [[3,6,9],[2,5,8],[1,4,7]]
#
# Parameters
# ----------
# matrix: List[List[int]]
#   A square matrix of ints
#
#
# Returns
# -------
# List[List[int]]
#   Returns parameter matrix rotated 90 degrees to the left
#
def rotate_matrix(matrix):
    pass

# Largest Sum Subarray
#
# Write a function that given an array of integers will return the continuous subarrray with the largest
# sum in the entire array
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [-8,-6,1,-4,3,4,6]
#   Output: [3,4,6]
#
# Example 2:
#   Input: [2,-8,7,-3,4,-20]
#   Output: [7,-3,4]
#
# Example 3:
#   Input: [-1,-2,-3,-4]
#   Output: [-1]
#
# Parameters
# ----------
# arr : List[int]
#   A variable length array of integers
#
# Returns
# -------
# List[int]
#   Largest sum continous sub array
#
def largest_sum_subarray(arr):
    pass

# String, My One True Love
#
# Your favorite course staff member really likes strings that have the same occurances of letters.
# This means the staff member likes "aabbcc" and "ccddee" and even strings like "abcabcabc"
#
# But "that one guy that wrote the pokomon problem" wants to trick the staff with really long string,
# that either could be the string that the staff member likes, or something that becomes such a string
# when you remove a single character from the string.
#
# Your goal is to return True if it's a string that the "one guy that wrote the pokomon problem" made
# and False otherwise.
#
# Restrictions
# ------------
# Inputs are only given as lower case alphabets, without punctuation, spaces, etc.
# Your solution must run in O(n) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: "abcbabcdcdda"
#   There is 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
#   Output:
#   True
#
# Example 2:
#   Input: "aaabbbcccddde"
#   Again there are 3 a's, 3 b's, 3 c's, and 3 d's. However, we also have 1 e!
#   We can remove this string however, and it will become a likeable string, so this is valid.
#   Output:
#   True
#
# Example 3:
#   Input: "aaabbbcccdddeeffgg"
#   This string is similar to the other ones, except with 2 e's, f's and g's at the end.
#   To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
#   one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
#   Output:
#   False
#
# Parameters
# ----------
# string : str
#   The string to check whether it is likeable or not.
#
# Returns
# -------
# bool
#   True if the string is likable, or removing a single character makes it likable.
#   False if the string is not likeable, and we need to remove more than 1 character to become likable.
def string_my_one_true_love(string):
    pass


# Gene Manipulation
#
# It's year 2050, and we have gotten advanced technology to manipulate genes at will.
# We consider a good gene to be when the "ATCG"s are balanced. That is for a gene length n,
# there are n/4 A's, T's, C's, and G's. Our technology allows us to "flash" the genes,
# replacing a subsequence of a gene with anything we want.
#
# Given a arbiturary gene, find the length of the minimum subsequence of the gene we need to flash
# to get a good gene.
#
#
# Restrictions
# ------------
# Inputs are only given as a string containing uppercase A, T, C, and Gs.
# The input size is always a multiple of 4 (or else we will never get a good gene)
# The genes can appear in any order.
#
# Your solution must run in O(n) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: "ATCGGATT"
#   We can remove the last T and change it to a C in order to make it a good gene.
#   Output:
#   1
#
# Example 2:
#   Input: "ATCGAAAAATCG"
#   We can remove the "AAA" and change it to a "CTG" in order to make it a good gene.
#   Output:
#   3
#
# Parameters
# ----------
# gene: str
#   The gene that we must find the subsequence to switch it out for
#
# Returns
# -------
# int
#    The length of the minimum subsequence in order to make the gene a good gene.
def gene_manipulation(gene):
    pass

# Longest Palindromic Substring
#
# Given a string, find the longest substring that is a palindrome. If
#
# Ideal runtime: o(n), but we will give full credit for o(n^2) solutions.
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest palindrome
#
# Example(s)
# ----------
# Example 1:
#   Input: "ABBAC"
#
#   Output:
#   "ABBA"
#
# Example 2:
#   Input: "A"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest Palindrome substring
def longest_palindrome_substring(word):
    pass

# Longest Unique Substring
#
# Given a string, find the longest unique substring
#
# Ideal runtime: o(n). full credit only given for o(n).
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest unique substring
#
# Example(s)
# ----------
# Example 1:
#   Input: "asdfawefABCDEFaabasfeasf"
#
#   Output:
#   "ABCDEF"
#
# Example 2:
#   Input: "AA"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest unique substring
def longest_unique_substring(word):
    pass

# Three Sum
#
# Given an array S of n integers, are there elements a, b, c in S such that
# a+b+c = 0? Find all unique triplets in the array which gives the sum of zero.
# return a 2d list, where all inner lists are triplets. There may be more than
# one pair of triplets.
#
# Runtime: o(n^2) will get full credit.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [-1, 0, 1, 2, -1, -4], 0
#
#   Output:
#   [
#  [-1, 0, 1],
#  [-1, -1, 2]
#   ]
#
#
# Parameters
# ----------
# arr: array
#   array of numbers
#
# target: int
#   target integer
#
# Returns
# -------
# 2d array
#    2d list, inner lists are triplets that add up to target.
def three_sum(arr, target):
    pass
