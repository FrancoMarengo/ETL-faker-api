FROM python:3.9.7-slim-bullseye

RUN pip install singer
RUN pip install target-csv
RUN pip install pyspark