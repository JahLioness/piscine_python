from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Description not available"

setup(
    name="ft_package",
    version="0.0.1",
    description="My first python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ede-cola",
    author_email="ede-cola@student.42.fr",
    url="https://github.com/JahLioness/ft_package",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
