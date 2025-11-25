FROM python:3.14.0-alpine3.22

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
