# BUILDING IMAGE: docker build -t $DOCKER_ID_USER/my-python-app .
# RUNNING IT: docker run -it --rm --name my-running-app $DOCKER_ID_USER/my-python-app
# PUSHING IT TO DOCKERHUB: docker login, docker push $DOCKER_ID_USER/my-python-app

FROM python:2

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./Main.py" ]
