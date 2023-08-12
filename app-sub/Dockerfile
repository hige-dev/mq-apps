FROM python:3.10-alpine

WORKDIR /app-sub
COPY requirements.txt /app-sub
RUN apk --no-cache add build-base postgresql-dev
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "mq_sub.py"]
