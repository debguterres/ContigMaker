#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys

try:
    from setuptools import find_packages, setup
except ImportError:
    sys.exit(
        "We need the Python library setuptools to be installed. "
        "Try runnning: python -m ensurepip"
    )


with open("README.md", "r") as readme_file:
    README = readme_file.read()


if __name__ == "__main__":
    setup(
        author="Débora Cervieri Guterres.",
        author_email="debora.guterres@gmail.com",
        name="ContigMaker",
        version="1.0.0",
        long_description=README,
        long_description_content_type="text/markdown",
        keywords=["Bioinformatics", "Sanger"],
        # url="https://github.com/",
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.10",
        options={"bdist_wheel": {"universal": True}},
        entry_points={
            "console_scripts": ["blu=src.main:main"],
        },
    )
