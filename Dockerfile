FROM tiangolo/meinheld-gunicorn-flask:python3.9

ADD VERSION .

COPY ./requirements.txt /app/requirements.txt

# Install Git
#RUN apt-get update && apt-get install -y git

# Copy files
COPY ./nirepage /app/nirepage/
COPY ./main.py /app/main.py

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt