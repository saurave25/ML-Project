from setuptools import find_packages, setup
from typing import List

hyphan_e_dot = '-e .'
def get_requirement(file_path:str)->List[str]:
    # this function will return the list of requiremnt

    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyphan_e_dot in requirements:
            requirements.remove(hyphan_e_dot)
    return requirements        


setup(
    name='mlproject',
    version='0.0.1',
    author='Saurav',
    author_email='saurave26@gmail.com',
    packages=find_packages(),
    install_requires= get_requirement('requirements.txt')
)