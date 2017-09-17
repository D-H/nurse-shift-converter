# ON MY END
# BUILDING IMAGE: docker build -t dchender/my-python-app .
# PUSHING IT TO DOCKERHUB: sudo docker login, docker push dchender/my-python-app

# ON THE OTHER END
# PULL IT TO DOCKERHUB: docker login, docker pull dchender/my-python-app
# RUNNING IT: sudo docker run -i -t -d --rm --name my-running-app dchender/my-python-app

FROM ubuntu:14.04

WORKDIR /usr/src/app

COPY . .

# Get cron scheduler
RUN apt-get update && apt-get install -y cron

# Get python
RUN apt-get install -y python-setuptools python-dev build-essential

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/converter

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/converter

# Give execution rights on the cron job
RUN /usr/bin/crontab /etc/cron.d/converter

# Create log for dockerfile
RUN touch /var/log/cron.log

# Start cron (done manually)
# sudo docker exec -it my-running-app bash
# CMD cron
