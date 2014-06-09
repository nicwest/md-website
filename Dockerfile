FROM ubuntu:precise
RUN apt-get -y update
RUN apt-get -y install python-pip
ADD . /var/www
COPY ./config-sample.py /var/www/config.py
RUN pip install -r /var/www/requirements.txt
EXPOSE 5000
WORKDIR /var/www
CMD python run.py

