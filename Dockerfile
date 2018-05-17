FROM python:3.6
MAINTAINER lushanjason
RUN git clone https://github.com/stkaeljason/crawler_manager.git
WORKDIR /crawler_manager
COPY dist /crawler_manager/dist
RUN pip3 install pipenv
RUN pipenv install
