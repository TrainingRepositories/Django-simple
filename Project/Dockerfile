FROM --platform=linux/amd64 python:3.10-slim AS production
# FROM  python:3.10-slim AS production


WORKDIR /app
  
# commons start 

RUN apt-get update \
    && apt-get install -y libpq-dev gcc openssl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip 

# commons end 


# app requirements

COPY ./requirements.txt app/requirements.txt
RUN  pip install --no-cache-dir -r app/requirements.txt
 
COPY ./start-reload.sh start-reload.sh
RUN chmod +x ./start-reload.sh 
# app requirements

COPY . .


ENTRYPOINT ["sh", "./start-reload.sh"]