## ML_CICD_pipeline
### softwares and accounts requirements

1. [Github Account](https://github.com/)
2. [Heroku Account](www.heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [GIT Cli](https://git-scm.com/docs/gitcli)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

creating comda environment
```
conda crate -p venv python==3.7 -y
```
```
conda activate venv/
```
```
pip install -r requirements.txt
```
git commands
```
git add .
git commit -m "commit messege"
git push origin main
```
To check remote url 
```
git remote -v
```
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To setup CI/CD pipeline in heroku we need 3 information
```
Heroku app name     : ml-app-pipeline
Heroku mail id      : harithushan3@gmail.com
Heroku API key      : <>  
```
Build docker image
```
docker build -t  <image_name>:<tagname> .
docker build -t  ml_app_pipeline:latest .
```
>Note : Name for docker image should be lowercase

to list docker image
```
docker images
```
run docker image
```
docker run -p 5000:5000  -e PORT=5000 72a821aebdd5
```
to check the running docker container
```
docker ps
```
to stopp the running docker container
```
docker stop <container_id>
``` 