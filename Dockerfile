
FROM python:3.7-alpine

COPY script.py /home/script.py

CMD [ "python", "script.py"]
