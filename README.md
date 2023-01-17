## ML_CICD_pipeline
### softwares and accounts requirements

1. [Github Account](https://github.com/)
1. [Heroku Account](www.heroku.com)
1. [VS Code IDE](https://code.visualstudio.com/)
1. [GIT Cli](https://git-scm.com/docs/gitcli)

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
Requirements for deployment
```
Heroku app name     : ml-app-pipeline
Heroku mail id      : harithushan3@gmail.com
Heroku API key      : 3f9fdd13-b91d-41ee-8fd7-3ded1235af66  
```
Build docker image
```
docker build -t  <image_name>:<tagname> .
docker build -t  al_app_pipeline:latest .
```
>Note : Name for docker image should be lowercase

to list docker image
```
docker images
```
run docker image
```
docker run -p 5000:5000  -e PORT=5000 ID
```
to check the running docker container
```
docker ps
```
to stopp the running docker container
```

``` 