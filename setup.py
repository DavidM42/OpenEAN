from setuptools import setup,setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='openean',
    version='0.1.1',
    description='Unofficial API wrapper for Open EAN/GTIN Database',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DavidM42/OpenEAN',
    author='DavidM42',
    author_email='david@merz.dev',
    license='MIT',
    # packages=['openean'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'])