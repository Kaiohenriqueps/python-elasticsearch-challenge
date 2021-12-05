FROM httpd

RUN apt-get update && apt-get install -y \
  apache2 python3 python3-pip vim \
  && apt-get clean

RUN mkdir /var/apache_flask
ADD . /var/apache_flask/
WORKDIR /var/apache_flask

RUN pip3 install -r requirements.txt

EXPOSE 5000
EXPOSE 8888