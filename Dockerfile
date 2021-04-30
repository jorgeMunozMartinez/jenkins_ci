FROM python:3.7-alpine

RUN pip install requests

COPY hello_there.py /usr/share/jenkins/script.py

CMD [ "python", "script.py"]
