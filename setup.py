import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorsimple",
    version="0.1.2",
    author="Cong Wang",
    author_email="wangimagine@gmail.com",
    description="A simple package to facilitate manipulation of colors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carbonscott/colorsimple",
    keywords = ['colors'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
