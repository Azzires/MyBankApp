FROM alpine:3.17.2
RUN apk add --no-cache bash
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install flask
WORKDIR /app
COPY . .
ENV FLASK_APP=main
EXPOSE 5000
CMD python3 main.py