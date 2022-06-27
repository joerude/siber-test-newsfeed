FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
COPY . /code/



#FROM python:3
#ENV PYTHONUNBUFFERED=1
#WORKDIR /usr/src/app
#COPY requirements.txt ./
#ADD entrypoint.sh /entrypoint.sh
#RUN pip uninstall django
#RUN pip install -r requirements.txt
#RUN chmod a+x /entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]
