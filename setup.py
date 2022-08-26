from setuptools import setup

# read the contents of your README file
from pathlib import Path
PATH = Path(__file__).parent
long_description = (PATH / "README.md").read_text()

setup(
        long_description = long_description,
        long_description_content_type = "text/markdown",
        package_dir= {'pythonsay': 'scr'},
    )

