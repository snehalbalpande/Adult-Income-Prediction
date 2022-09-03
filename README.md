# Adult-Income-Prediction
This is adult income prediction project

Creating conda environment

'''conda create -p venv python==3.9 -y'''

'''conda activate venv/
'''
OR

'''conda activate venv'''

'''pip install -r requirements.txt'''

To Add files to git

'''git add .'''
OR

'''git add <file_name>'''
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

'''git status'''

To check all version maintained by git

'''git log'''

To create version/commit all changes by git

'''git commit -m "message"'''

To send version/changes to github

'''git push origin main'''

To check remote url

'''git remote -v'''

To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = snehalbalpande1@gmail.com
HEROKU_API_KEY = 2bee9681-63c3-472a-b214-280b8e8b7606
HEROKU_APP_NAME = meachine-learning-app

BUILD DOCKER IMAGE

'''docker build -t <image_name>:<tagname> .'''

Note: Image name for docker must be lowercase

To list docker image

'''docker images'''

Run docker image

'''docker run -p 5000:5000 -e PORT=5000 f8c749e73678'''

To check running container in docker

'''docker ps'''

Tos stop docker conatiner

'''docker stop <container_id>'''

'''python setup.py install'''

Install ipykernel

'''pip install ipykernel'''

Data Drift :
When your dataset stats gets change we call it as data drift


# Write a function to get training file path from artifact dir