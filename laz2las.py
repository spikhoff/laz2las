import sys
import os
import glob
import laspy

# Get all LAZ files in the current directory
laz_files = glob.glob("*.laz")

for laz_file in laz_files:
  # Extract filename without extension
  file_name, _ = os.path.splitext(laz_file)

  # Create output file path with .las extension
  output_file = f"{file_name}.las"

  # Read LAZ file
  las = laspy.read(laz_file)

  # Write LAS file
  las.write(output_file)

  print(f"Converted {laz_file} to {output_file}")
  
