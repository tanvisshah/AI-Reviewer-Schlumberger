FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN echo "uwsgi_read_timeout 300s;" > /etc/nginx/conf.d/custom_timeout.conf
# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;

ENV STATIC_PATH /app/app/static

RUN apt-get install libreoffice -y
RUN apt-get install poppler-utils -y
COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /var/www/requirements.txt

#COPY . /app