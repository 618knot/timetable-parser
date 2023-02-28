FROM centos/python-38-centos7:latest
USER root
WORKDIR /app
COPY ./timetable-parser/docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN yum -y install java-1.8.0-openjdk

RUN pip install --no-cache-dir uvicorn