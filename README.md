# Exoflow
Python Module for advanced image editing.

# Features
1. Spill image pixels in direction specified by a 2d vector.
2. Merge multiple images.

# Installation
Download current build from: https://pypi.python.org/pypi/exoflow

Run the following command inside the downloaded directory:
python setup.py install

# Tutorial
import exoflow as ef

a = ef.Session('./path_of_image/image_name.jpg', './path_of_output_file/name_of_output_file.jpg') #the output file should be the exact copy of the input image, just make a copy of the input image prehand.

a.spill(1, 2, 20)

a.save()

# Contributions
1. Find bugs and issues.
2. Fix bugs and issues.
3. Implement features.
4. Suggest new features.
