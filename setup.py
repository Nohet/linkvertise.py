from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="linkvertise",
    version="1.1.5",
    packages=["linkvertise"],
    description="Python wrapper for linkvertise monetizing api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nohet/linkvertise.py",
    author="Nohet",
    author_email="igorczupryniak503@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="linkvertise, linkvertise wrapper, linkvertise api, linkvertise monetizing",

)
