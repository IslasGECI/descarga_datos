mutants: install
	mutmut run --paths-to-mutate descarga_datos

.PHONY: \
    clean \
    format \
    install \
    mutants \
    tests \

clean:
	rm --force --recursive .mutmut-cache
	rm --force --recursive .pytest_cache
	rm --force --recursive $$(find . -name '__pycache__')

format:
	black --check descarga_datos
	black --check tests

install:
	pip install --editable .

tests:
	pytest --cov=descarga_datos --cov-report=term --verbose
