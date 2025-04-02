from setuptools import find_packages, setup
from typing import List

Hyphen = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:  # Fixed file_path usage
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]  # Using strip() instead of replace('\n', '')

        if Hyphen in requirements:  # Fixed case issue
            requirements.remove(Hyphen)

    return requirements

setup(
    name="ML Project",
    version="0.0.1",
    author="Charity",
    author_email="nyamucc@clarkson.edu",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Fixed argument
)
