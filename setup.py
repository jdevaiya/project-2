"""
    this setup.py file is an essential part of packaging and 
    distributing Python projects. It is used by setuptools 
    (or distutils is order python versions) to define the configuration
    of your project, such as its metadata, dependebcies, and more 
"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    """
    this function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read line from the file
            lines = file.readlines()
            # Process each line 
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Jayendra Devaiya",
    author_email="jdevaiya2175@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
