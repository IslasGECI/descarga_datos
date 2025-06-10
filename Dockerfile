FROM python:3.12
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut \
    pylint \
    pytest \
    pytest-cov
