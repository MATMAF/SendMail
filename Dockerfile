FROM python:3.12.1-slim

EXPOSE 5000

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ["python", "SendMail.py"]
