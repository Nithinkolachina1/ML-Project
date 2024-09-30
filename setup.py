from setuptools import find_packages, setup
from typing import List
import os

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    try:
        print(f"Reading requirements from: {os.path.abspath(file_path)}")  # Debugging file path

        requirements = []
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n", "") for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)

        print(f"Requirements: {requirements}")  # Debugging output
        return requirements
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
        return []

setup(
    name='ML Project',
    version='0.0.1',
    author='Nithin',
    author_email='nithinkolachina1007@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
