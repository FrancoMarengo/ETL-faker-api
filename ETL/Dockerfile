FROM python:3.9.7-slim-bullseye

WORKDIR /ETL
COPY . .

RUN pip install numpy pandas requests

ENTRYPOINT ["python"]

CMD ["asd.py"]
