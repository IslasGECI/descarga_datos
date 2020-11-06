FROM python:3.8
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
CMD make
