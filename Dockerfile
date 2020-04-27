FROM python:3
COPY . /workdir/
WORKDIR /workdir
RUN pip install \
    codecov \
    mutmut \
    pytest \
    pytest-cov
CMD make
