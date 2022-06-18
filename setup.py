from setuptools import setup
from typing import List

#declaring variable for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Gyanendra"
DESCRIPTION="This is a first FSDS Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->list[str]:
    """
    Description: This function is going to return the list of requirement mention in requirement.txt file
    return: This is going to return a list which contain name of libraries mentioned in reuirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    insatll_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())

