FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* 

WORKDIR /code
COPY requirements /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
#RUN bash && \
#   chmod 777 ./wait.sh
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz

ENTRYPOINT ["dockerize", "-wait", "tcp://db:3306", "-timeout", "20s"]