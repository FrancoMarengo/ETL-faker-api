FROM python:3.9.7-slim-bullseye

WORKDIR /ETL
COPY . .

RUN pip install singer-python
RUN pip install target-csv

RUN pip install numpy pandas requests

ENTRYPOINT ["python"]

CMD ["tap_fake_api.py"]