import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kuys-vemboy",
    version="0.0.1",
    author="Vem Papazian",
    author_email="vem@papazian.info",
    description="A color manipulation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vemboy/Kuyn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)