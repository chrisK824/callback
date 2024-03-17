from setuptools import setup, find_packages

setup(
    name='callback-factory',
    version='0.0.2',
    description='A simple Python library for producing parameterized and flexible callbacks that can be overriden during execution',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chrisK824/callback",
    author='Chris Karvouniaris',
    author_email="christos.karvouniaris247@gmail.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    python_requires='>=3.5',
    license_files=["LICENSE"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
