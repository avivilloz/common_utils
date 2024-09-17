from setuptools import setup, find_packages

setup(
    name="common_utils",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description=(
        "This is a Python package that offers a comprehensive set of utility "
        "functions for string manipulation, file operations, and directory "
        "management. It simplifies common tasks in text processing and file "
        "system interactions, enhancing productivity in various Python "
        "projects."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/common_utils",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
