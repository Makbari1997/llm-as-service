FROM python:3.8.10 as builder
LABEL description="RoBERTa for Intent Detection"
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/

# Downloading .h5 file of finetuned model
RUN apt-get update && apt-get install -y wget
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-lFF3vM-ZiUlhLl6ccc-6ZmcgnO3OdJR' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-lFF3vM-ZiUlhLl6ccc-6ZmcgnO3OdJR" -O /app/roberta-finetuned/tf_model.h5 && rm -rf /tmp/cookies.txt

# test whether everything is ok
RUN pytest

# running endpoint
EXPOSE 8000
CMD ["python", "app.py"]