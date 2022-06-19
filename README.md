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

Second we need to work on Entity.

Steps in Machine Learning Pipeline
1. Data Ingestion (feom AWS, GCP, Azure etc) (Split data into training and testing)
2. Data Validation
    i) Schema Validation
    ii) Duplicate
    iii) NULL Check
    iv) Imbalance Data
    v) Data Range
    vi) Domain value --excepted value of column
    vii) Anamolies
    viii) Data Drift --change in data
After this we can perform the EDA to understnad data --jupyter
3. Data Transformation/Feature Engineering (keep pickle object)
4. Model Training (keep pickle object) (Model Comparision)
    i) Model Selection -- jupyter
    ii) Hyperparameter Tuning --jupyter
5. Model Evaluation (Test Data for Model Evaluation) (Model Comparision --best model and minimum expectation)
6. Push Model

Note: Saving object into file is called as serialization and loading object fromm file is called as deserialization.
 We can create pickle for any class not only for model.

 Pass test data to pickle object of feature engineering and then through modek to check model performance.

 Real world Data --> Pickle Object of feature Enginerring (Transform function) --> Pickle object of model training (Prediction function) --> Prediction

Note: Create Final pickle file with Feature Engineering object, model Object that we need to deploy

MLOps
{
DevOps: 
{
    DevOps is the combination of cultural philosphies, practices, and tools that increases an organisations ability to deliver applications and services at high velocity.

    CI+CD and Code Versioning
}
Data Versioning and Contineous Training (CT)
}

Data Versioning: Hash value and Timestamp is used for data versioninng.

Entity: 
Artificat is defined for each component of pipeline.

DataIngestionArtifact
DataValidationArtifact
DataTransformationArtifact
ModelEvaluationArtifact
ModelPusherArtifact
ModelTrainerArtifact

DataIngestionConfig
DataValidationConfig
DataTransformationConfig
ModelEvaluationConfig
ModelPusherConfig
ModelTrainerConfig


Config:
config.yaml --configuration details
schema.yaml --schema details
database --database details

