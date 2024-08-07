**laz2las**

**A Python script to convert LAZ files to LAS format, with error handling and improved functionality.**

### Usage

```bash
python laz2las.py [options] <LAZ_files>

# Example: Convert all LAZ files in the current directory
python laz2las.py *.laz

# Example: Convert specific LAZ files and specify output directory
python laz2las.py --output_dir /path/to/output data_1.laz data_2.laz
```

**Options:**

* `-o`, `--output_dir`: Specify the directory to write the LAS files. Defaults to the current directory.

### Dependencies

* laspy

### Installation

Ensure you have Python and the `laspy` library installed:

```bash
pip install laspy
```

### How it Works

The script iterates through provided LAZ files or all LAZ files in the current directory (if no files are specified). It reads the LAZ data using the `laspy` library and writes the data to a new LAS file with the same name but a `.las` extension. The script also includes the following improvements:

* **Error handling:** Handles potential errors like missing LAZ files or issues during conversion.
* **File existence check:** Checks if the output LAS file already exists to avoid overwriting data unintentionally.
* **Informative messages:** Provides clear messages about successful conversions and encountered errors.

### Example

If you have the following LAZ files in your current directory:

* `data_1.laz`
* `data_2.laz`

Running the script with `python laz2las.py *.laz` will create the following LAS files in the current directory:

* `data_1.las`
* `data_2.las`

**Note:** This script is designed for basic conversion and can be further customized for specific needs.

### Unit Tests

The script includes unit tests to ensure its functionality and reliability.

### Contributing

We welcome contributions to improve this script. Feel free to submit pull requests with enhancements or bug fixes.
