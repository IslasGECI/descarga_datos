FROM python:3.12
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    geci-test-tools \
    mutmut==2.5.1 \
    pylint \
    pytest \
    pytest-cov
