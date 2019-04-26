import os.path
from setuptools import setup, find_packages

VERSION = "0.1.0"
HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="pyteams",
    version=VERSION,
    description="Helper library to construct microsoft teams connector cards",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/HarshadRanganathan/pyteams",
    author="Harshad Ranganathan",
    author_email="rharshad93@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="Microsoft Teams",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "images"]),
    install_requires=[
        "jsonpickle"
    ],
    python_requires='>=3.7',
)
