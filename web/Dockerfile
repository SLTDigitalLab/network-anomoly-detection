
FROM python:3.11.2-buster

RUN mkdir build

WORKDIR /build

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

WORKDIR /build/app

CMD gunicorn -w 4 'app:app'

