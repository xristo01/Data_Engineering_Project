from setuptools import setup
from setuptools import find_packages

setup(
    name='HristoScraper', ## This will be the name your package will be published with
    version='0.0.5',
    description='This is a car price scraper package',
    url='https://github.com/xristo01/Data_Engineering_Project', # Add the URL of your github repo if published
    # in GitHub
    author='Hristo Petkov', # Your name
    license='MIT',
    packages=find_packages(), # This one is important to explain. See the notebook for a detailed explanation
    install_requires=['pandas', 'selenium', 'numpy'], # For this project we are using two external libraries
# Make sure to include all external libraries in this argument