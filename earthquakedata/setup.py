from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Build an automated ETL pipeline to fetch, process, and store earthquake data from the USGS API',
    author='Maryam Gholamicherovi',
    license='MIT',
)
