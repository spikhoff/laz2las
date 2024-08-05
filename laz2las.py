import sys
import os
import laspy

# Get the input file name with path
input_file = sys.argv[1]

# Extract the file name without extension
file_name, _ = os.path.splitext(input_file)

# Create the output file path with .las extension
output_file = f"{file_name}.las"

# Read the LAZ file
las = laspy.read(input_file)

# Write the LAZ data to the LAS file
las.write(output_file)

print(f"Converted {input_file} to {output_file}")
