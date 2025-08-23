FROM python:3.10

WORKDIR /app

COPY . /app

ENV PYTHONPATH=/app/airflow/scripts


RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r airflow/scripts/requirements.txt


CMD ["python", "airflow/scripts/table_insertion.py"]
