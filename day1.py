
""" Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:

1. Declare  variables: one of type int, one of type double, and one of type String.
2. Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
3. Use the  operator to perform the following operations:
    - Print the sum of  plus your int variable on a new line.
    - Print the sum of  plus your double variable to a scale of one decimal place on a new line. """

#TODO: This solution failed one of the two test cases(i+j=7, when i=3), figure out why.


i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
j = 12
e = 4.0
t = 'is the best place to learn and practice coding!'
# Read and save an integer, double, and String to your variables.
def SumOfInteger():
    return print(i + j)
    
def SumOfFloat():
    return print(d + e)
    
def ConcatenateString():
    return print(f"{s}{t}")
    
# Print the sum of both integer variables on a new line.
SumOfInteger()
# Print the sum of the double variables on a new line.
SumOfFloat()
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
ConcatenateString()
