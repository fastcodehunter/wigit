
FROM python:3.12





COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . /code
WORKDIR /code



EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]