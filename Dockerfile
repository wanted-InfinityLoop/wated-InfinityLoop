FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
# CMD ["python", "./app.py"]
# CMD ["gunicorn :app", "--bind", "0.0.0.0:8000"]