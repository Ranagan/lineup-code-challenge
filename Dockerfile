FROM python:3.10-bullseye

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./app /code/app

RUN pip install "uvicorn[standard]"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
