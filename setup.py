from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    Read function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        return requirements

setup(
    name='MLProject',
    version='0.1.0',
    author='Sonu Kumar Suman',
    author_email='sonukumarsuman82@gmail.com',
    packages=find_packages(),
    install_requires=['numpy', 'pandas']
)
