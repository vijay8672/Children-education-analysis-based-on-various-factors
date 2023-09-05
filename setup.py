## Python setup.py 

"""
It is used for building our application as a package itself, so that we can reuse the when ever it is necessarily required

setup.py is a Python script used to define the metadata and configuration for a Python package. 
This script is typically used in conjunction with the setuptools library 
to create distributable Python packages that can be easily installed using tools like pip. 
"""

## Code 

from setuptools import setup, find_packages
from typing import List

# Avoid naming conflicts by renaming your 'typing.py' file
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Corrected: Modify the 'requirements' list in place
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='MACHINE LEARNING PROJECT ON CHILDREN EDUCATION AFFECTED BY VARIOUS FACTORS',  # Changed 'Project_Name' to 'name'
    version='0.0.1',
    author='Vijay Kumar Kodam',
    author_email='vijay.kodam98@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
