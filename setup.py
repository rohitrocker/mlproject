from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:  # ✅ Works everywhere

    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]



    if '-e .' in requirements:
         requirements.remove('-e .')
    return requirements


setup(
    name='project1',
    version='0.0.1',
    author='rohit',
    author_email='thakurrohit0555p@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)