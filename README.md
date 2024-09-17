# Common Utils

This is a Python package that offers a comprehensive set of utility functions for string manipulation, file operations, and directory management. It simplifies common tasks in text processing and file system interactions, enhancing productivity in various Python projects.

## Description:

This Python package is a versatile collection of utility functions designed to streamline common operations in Python development. It provides a wide range of functionalities, including:
- Text Processing: Functions for word counting, quote removal, newline handling, space management, and punctuation removal.
- String Formatting: Utilities for converting strings to file names or tag names, and formatting index numbers.
- File Operations: Tools for reading files, both entire contents and line-by-line.
- Directory Management: Functions to list file and directory paths, create or remove directories, and copy or move files.
- Path Handling: Utilities to check path existence and list various aspects of directory contents.
- Sentence Analysis: Functions to count sentences and split text into individual sentences.

This package is designed with simplicity and efficiency in mind, making it an invaluable tool for developers working on projects that involve text manipulation, file system operations, or general Python scripting. By centralizing these common utilities, common_utils promotes code reusability and maintains consistency across different parts of a project or even across multiple projects.

The package also incorporates error handling and logging, ensuring robust performance and easier debugging. Whether you're developing a small script or a large-scale application, common_utils can significantly reduce the amount of boilerplate code and improve overall code quality.


## How to install:

Run the following command in your python venv:

```bash
pip install git+https://github.com/avivilloz/common_utils.git@main#egg=common_utils
```

Or add the following line to your project's `requirement.txt` file:

```
git+https://github.com/avivilloz/common_utils.git@main#egg=common_utils
```

And run the following command:

```bash
pip install -r requirements.txt
```

## How to use:

```python
from common_utils import *

# Use common methods
```