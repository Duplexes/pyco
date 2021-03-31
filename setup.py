import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyconsole",
    version="0.6",
    author="Duplexes and LemonPi314",
    author_email="49930425+LemonPi314@users.noreply.github.com",
    description="Some tools for printing with colors in the console, as well as logging functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Duplexes/pyconsole",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
)