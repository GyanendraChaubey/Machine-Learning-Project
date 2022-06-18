# Machine-Learning-Project
This is complete  project
Conda create -p venv python==3.7 -y

"""
"""
#To acmenttive environ
conda activate venv/
"""

pip install -r requirements.txt

"""
To check git status 

git log -- to provide git log

"""

"""
To add file to git

git add file_name
"""

Note: To ignore file and folder from git we can write it in .gitignore file

"""
To create version/commit all changes by git

git commit -n "message"

"""

"""
to send version/changes to github

git push origin main

"""

"""
To Check remote url

git remote -v

"""

"""
To create CICD pipeline Need three things

API Key: xxxx
App name: ml-regression-application
Heroku Email: gyanendrachaubey68@gmail.com

"""

"""
BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname>

"""

> Note: Image name for docker file must be a lowercase

"""
To list docker images

>docker image

"""

"""
Run docker image

> docker run -p 5000:5000 -e PORT=5000 

"""

"""
To check Running container in docker

> docker ps

"""

"""
To stop docker 

docker stop <container_id>

"""
"""
pip install -r requirements.txt
"""

Folder Structure
Housing
    --> __init__.py
    --> exception package
    --> logger package
    --> pipeline package
    --> stages package
    --> config package
    --> entity packages
    --> component/src packaages

Logger and Exception need to work first.