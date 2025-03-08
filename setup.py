import setuptools
from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# package setup
setup(
    name="masto",
    version="2.0.6", 
    author="OSINT_Tactical (AKA C3n7ral051nt4g3ncy)",
    author_email="C3n7ral051nt4g3ncy@tactical-osint-academy.com",
    description="Masto OSINT Tool Python package for Mastodon user investigations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/C3n7ral051nt4g3ncy/Masto",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "bs4",
        "tqdm",
        "urllib3",
        "argparse",
        "w3lib",
        "aiohttp",
        "asyncio",
        "requests",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "masto=masto.masto:main",  # running masto from CLI
        ],
    },
)
