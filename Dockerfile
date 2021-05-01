FROM python:3.7-alpine

RUN pip install requests

COPY script.py /

CMD [ "python", "script.py"]
