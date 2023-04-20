FROM alpine:3.17.2
RUN apk add --no-cache bash
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install flask
RUN pip3 install gunicorn
WORKDIR /app
COPY . .
ENV FLASK_APP=app
CMD gunicorn --workers 3 --bind 0.0.0.0:8000 -m 007 wsgi:app