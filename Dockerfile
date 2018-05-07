FROM python:3.6
USER jason
WORKDIR /home/jason/
RUN apt-get install python3-pip
RUN pip3 install pipenv
RUN git clone 
WORKDIR /home/jason/crawler_manager 
RUN pipenv install

