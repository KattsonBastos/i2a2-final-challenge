FROM python:3.8

COPY ./main /main

COPY ./requirements.txt /requirements.txt

RUN mkdir ~/.streamlit

COPY ./config.toml ~/.streamlit/config.toml
COPY ./credentials.toml ~/.streamlit/credentials.toml

RUN pip install -r requirements.txt

EXPOSE 5000

WORKDIR /main

CMD ["sh", "-c", "streamlit run --server.port $PORT app.py"]
