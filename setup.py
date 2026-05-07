from typing import List
from setuptools import setup,find_packages

hypen_e_dot='-e.'

def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

        return requirements
    

from typing import List


# Better version for future as it is performing good work
# def get_requirements(file_path: str) -> List[str]:
#     requirements = []
#     with open(file_path) as file_obj:
#         for line in file_obj:
#             line = line.strip()

#             if line and not line.startswith("#") and line not in ["-e .", "-e."]:
#                 requirements.append(line)

#     return requirements




setup(
   name='ML_Project',
   version='0.0.1',
   description='My Project',
   author='Shivam',
   author_email='shuklashivam@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt')
)
