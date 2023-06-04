FROM tiangolo/meinheld-gunicorn-flask:python3.9

COPY ./requirements.txt /app/requirements.txt

# Install Git
#RUN apt-get update && apt-get install -y git

# Clone the GitHub repository
#RUN git clone https://github.com/PaU1570/pauluv.com /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt