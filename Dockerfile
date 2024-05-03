# Dockerfile with APMA NEWSLETTER GENERATOR
# author: Micha Birklbauer
# version: 1.0.0

FROM python:3.12.0

LABEL maintainer="micha.birklbauer@gmail.com"

RUN mkdir app
COPY ./ app/
WORKDIR app
RUN pip install -r requirements.txt

CMD  ["streamlit", "run", "streamlit_app.py"]
