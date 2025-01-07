from setuptools import find_packages,setup
from typing import List
##try to read the requirements
#try to read file in the format os str and -> is return type list in str
HYPEN_E_DOT='-e .'# -e is present in the requirement.txt it should be trigger the set.up file this not module
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        ##read line by line
        requirements=file_obj.readlines()
        ##remove /n from every line
        [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
    
setup(
    name='RegressorProject',
    version='0.0.1',
    author='Saroja',
    author_email='Sarojayadhaiah2224@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)