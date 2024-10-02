#!/home/youli/miniconda3/bin/python
# coding=utf8
"""
# Author: youli
# Created Time : 2024-10-02 19:20:59

# File Name: change_f90_to_f77.py
# Description:

"""
def convert_continuation_f90_to_f77(file_f90, file_f77):
    """
    Convert Fortran 90 continuation lines to Fortran 77 format and enforce
    that the first 5 columns are spaces (with special character in column 6 for continuation).
    
    :param file_f90: Path to the Fortran 90 input file
    :param file_f77: Path to the Fortran 77 output file
    """
    
    with open(file_f90, 'r') as f90_file:
        f90_lines = f90_file.readlines()
    
    f77_lines = []
    continuation = False

    for i, line in enumerate(f90_lines):
        stripped_line = line.rstrip()

        # Ensure first 5 columns are spaces, preserving necessary characters in column 6+
        if len(stripped_line) > 0:
            # Strip leading spaces and add 5 initial spaces
            line = '      ' + stripped_line.lstrip()

        if continuation:
            # Insert a continuation character ('&') in the 6th column for F77
            line= '     &' + stripped_line.lstrip() 
            continuation = False

        # Check if the line ends with '&', indicating a continuation line in F90
        if stripped_line.endswith('&'):
            # Remove the '&' at the end of the line
            line = line[:-1] 
            # Add spaces to enforce Fortran 77 rule
            continuation = True
        f77_lines.append(line+'\n')

    # Write the converted F77 code to the output file
    with open(file_f77, 'w') as f77_file:
        f77_file.writelines(f77_lines)


if __name__ == "__main__":
    import sys
    input_f90 = str(sys.argv[1])  # Replace with your input F90 file path
    output_f77 = str(sys.argv[2])  # Replace with your desired output F77 file path
    convert_continuation_f90_to_f77(input_f90, output_f77)

