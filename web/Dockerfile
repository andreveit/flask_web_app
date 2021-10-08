FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
# CMD python app.py
CMD gunicorn --workers=3 --bind=0.0.0.0:5000 app:app
