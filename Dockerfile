FROM python:3.8    

COPY requirements.txt /app/
WORKDIR  /app
RUN pip install -r requirements.txt 
COPY . /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000" ]
