FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    mutmut \
    pytest \
    pytest-cov
CMD make
