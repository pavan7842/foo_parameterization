from setuptools import setup, find_packages

setup(
    name="foo_parameterization",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Pavan",
    author_email="m.pavanchary@gmail.com",
    description="A package to calculate the Foo et al. parameterization for sphere volumes",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pavan7842/foo_parameterization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
