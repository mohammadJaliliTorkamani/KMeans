FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src
COPY data/ /app/data

RUN mkdir -p /app/output

ENV COLUMNS=revenue,runtime,vote_average,vote_count

WORKDIR /app/src