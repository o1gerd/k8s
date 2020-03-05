FROM python:3.8-slim
MAINTAINER Alexander Cheremukhin <cheremuhin@gmail.com>
WORKDIR /usr/src/app
RUN pip3 install datetime
RUN pip3 install bottle
COPY py3web.py .
EXPOSE 32400
CMD [ "python3", "./py3web.py" ]