FROM python:3.6
#RUN apt-get install python3-pip
RUN pip3 install pipenv
RUN git clone https://github.com/stkaeljason/crawler_manager.git
WORKDIR /crawler_manager 
RUN pipenv install
EXPOSE 5000
#CMD python app.py
