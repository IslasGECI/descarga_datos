FROM python:3
RUN pip install \
    codecov \
    pytest \
    pytest-cov
