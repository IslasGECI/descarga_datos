FROM python:3
COPY . /workdir/
WORKDIR /workdir
RUN pip install \
    codecov \
    pytest \
    pytest-cov
CMD make
