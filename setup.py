from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function return list of requirements
    """
    requirement_list:List[str] = []
    return requirement_list

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """

setup(
    name="sensor",
    version="0.0.1",
    author="Pramod Shendage",
    author_email="pramod.applausetester@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),    #[]
)