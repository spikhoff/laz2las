import sys
import os
import glob
import laspy

def convert_laz_to_las(laz_file, output_dir="."):
  """Converts a single LAZ file to LAS format.

  Args:
      laz_file (str): Path to the LAZ file.
      output_dir (str, optional): Directory to write the LAS file. Defaults to current directory.

  Returns:
      bool: True if conversion successful, False otherwise.
  """
  try:
    # Extract filename without extension
    file_name, _ = os.path.splitext(laz_file)

    # Create output file path with .las extension
    output_file = os.path.join(output_dir, f"{file_name}.las")

    # Check if output file already exists
    if os.path.exists(output_file):
      print(f"Skipping {laz_file}, {output_file} already exists.")
      return True

    # Read LAZ file
    las = laspy.read(laz_file)

    # Write LAS file
    las.write(output_file)

    print(f"Converted {laz_file} to {output_file}")
    return True

  except Exception as e:
    print(f"Error converting {laz_file}: {e}")
    return False

def main():
  """Main function for command line execution."""
  if len(sys.argv) > 1:
    # Get LAZ files from arguments (excluding script name)
    laz_files = sys.argv[1:]
    output_dir = "."  # Use current directory by default
  else:
    # Get all LAZ files in current directory
    laz_files = glob.glob("*.laz")
    output_dir = "."  # Use current directory by default

  for laz_file in laz_files:
    convert_laz_to_las(laz_file, output_dir)

if __name__ == "__main__":
  main()
