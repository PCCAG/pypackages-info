from setuptools import setup, find_packages

setup(
    name="pypackage-info",
    version="0.0.1",
    packages=find_packages(),
    author="PCCAG",
    description="A simple tool. Can output the name, version, last modified time, and location of the installed module in the current environment in a tabular form at the terminal.",
    entry_points={
        "console_scripts": [
            "pypackage-info = pypackage_info.info:main",
        ]
    },
)
