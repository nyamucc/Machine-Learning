from setuptools import find_packages,setup
from typing import List

Hyphen= '-e .'
def get_requirements(file_path:str)->List[str]:
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace ('\n', '')for req in requirements]
        
        if Hyphen in requirements:
            requirements.remove(Hyphen)

    return requirements

setup(
name='machine learning',
version='0.01',
author='Charity',
author_email='cherrynyamu@gmail.com',
packages=find_packages(),
install_requires=get_requirements('Requirements.txt')
)