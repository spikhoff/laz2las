### laz2las

**A Python script to convert LAZ files to LAS format.**

### Usage

```bash
python laz2las.py *.laz
```

This script will convert all LAZ files in the current directory to LAS format, preserving the original file name with a `.las` extension.

### Dependencies

* laspy

### Installation
Ensure you have Python and the `laspy` library installed:

```bash
pip install laspy
```

### How it works
The script iterates through all LAZ files in the current directory, reads the LAZ data using the `laspy` library, and writes the data to a new LAS file with the same name but a `.las` extension.

### Example
If you have the following LAZ files in your current directory:

* `data_1.laz`
* `data_2.laz`

Running the script will create the following LAS files:

* `data_1.las`
* `data_2.las`

**Note:** This script is a basic implementation and might require additional features or error handling for production use.
