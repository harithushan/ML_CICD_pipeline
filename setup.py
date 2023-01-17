from setuptools import setup
from typing import List

#Declaring  variables for setup function
Project_name ="housing predictor"
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
        requirement_file.readlines()


setup(
    name=Project_name,
    version=Version,
    author=Author,
    description=Description,
    packages=Packages,
    install_requires =get_requirements_list()
)