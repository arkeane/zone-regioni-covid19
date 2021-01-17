import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covid-zone", # Replace with your own username
    version="1.0",
    author="Ludovico Pestarino",
    author_email="ludovicopestarino00@gmail.com",
    description="Web App per colore regioni italiane restrizioni covid-19",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arkeane/zone-regioni-covid19",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
