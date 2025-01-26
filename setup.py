from setuptools import find_packages,setup
from typing import List

## for this List is not recognizeable so we will install the library over here : 
## basically my function will return the list 
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements from the given file path.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name = 'ML-Project',
version = '0.0.1',
author = 'Aayush',
author_email = 'kotakaayush5@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)

## 1. 
## the work of this get_requirements is that what path i am getting over here 
## and what ever libraries shoul be in thee requirements.txt will read it and get installed it 

##2. 
## so here when we are calling the requirements.txt files for installing the packages 
## the setup.py file will also run to make the packages as well : 
## to enabling there we will specificallyy write the -e . in the requremnts.txt file 

##3.
## so here when we are applying the fuction it will also read the -e . in the 
## requiremnts.txt file so to not read it write the code in ythe fxn : requiremts:
## if we also read the -e . file it will connect the setup.py file with that : 