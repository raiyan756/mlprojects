from setuptools import find_packages,setup
from typing import List
HYPEN_='-e .'
def get_req(file_path:str)->List[str]:
   requirements=[]
   with open(file_path) as file_obj:
      requirements=file_obj.readline()
      requirements=[req.replace('\n',"") for req in requirements] 
      if HYPEN_ in requirements:
         requirements.remove(HYPEN_)

         return requirements,


setup(
    name='mlprojects',
    version='0.0.1',
    author='Raiyan',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
    
)