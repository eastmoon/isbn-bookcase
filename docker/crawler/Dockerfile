FROM python:3

ADD .dependencies /
RUN \
    pip install -r .dependencies && \
    rm .dependencies

WORKDIR /repo
