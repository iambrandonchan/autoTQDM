FROM python
COPY . /progressifier
WORKDIR /progressifier
RUN apt-get update
RUN apt-get install -y vim
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

