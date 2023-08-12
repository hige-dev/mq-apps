FROM python:3.10-alpine

WORKDIR /app-pub
COPY requirements.txt /app-pub
RUN apk --no-cache add build-base postgresql-dev
RUN python -m pip install -r requirements.txt

COPY . .

CMD ["python", "server.py"]
