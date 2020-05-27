mutants: install
	mutmut run --paths-to-mutate descarga_datos

.PHONY: \
    clean \
    install \
    mutants \
    tests \

clean:
	rm --force --recursive .mutmut-cache
	rm --force --recursive .pytest_cache
	rm --force --recursive $$(find . -name '__pycache__')	

install:
	pip install --editable .

tests:
	pytest --cov=descarga_datos --cov-report=term --verbose
