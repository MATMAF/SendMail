FROM python:slim

EXPOSE 5000

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "SendMail.py"]
