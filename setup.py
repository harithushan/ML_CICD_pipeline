from setuptools import setup,find_packages
from typing import List
import setuptools

#Declaring  variables for setup function
Project_name ="housingpredictor"
Version = "0.0.1"
Author ="Paramanathan Thushanthan"
Description = "This is my machine learning project on housing prediction during the course study"
Packages =["housing"]
Requirements_file_name="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description  : This function is going to return list of requiremetns mentioned in the requirements.txt file
    
    return  this function is goin to return a list which contains name of the libraries  mentioned in the requirements.txt 
    """
    with open(Requirements_file_name)as requirement_file :
        return requirement_file.readlines().remove("-e .") #removing "-e ." here because find_packages() will also do the job of this

# packages=find_packages()# can also be used
setuptools(
    name=Project_name,
    version=Version,
    author=Author,
    description=Description,
    packages=find_packages(),#Packages#["housing"]
    install_requires =get_requirements_list()
)