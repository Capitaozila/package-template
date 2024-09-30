from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="Luis Brasil",
    author_email="luisdevtoo@gmail.com",
    description="A package to process images.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Capitaozila/package-template.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
