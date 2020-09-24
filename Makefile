all: mutants

repo = descarga_datos
codecov_token = ed02def2-1ad1-4e23-81cc-0ede5dac22a7

.PHONY: all clean format install lint mutants tests

check:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests

clean:
	rm --force .mutmut-cache
	rm --recursive --force ${repo}.egg-info
	rm --recursive --force ${repo}/__pycache__
	rm --recursive --force test/__pycache__

format:
	black --line-length 100 ${repo}
	black --line-length 100 tests

install:
	pip install --editable .

lint:
	pylint ${repo}
	pylint tests

mutants:
	mutmut run --paths-to-mutate ${repo}

tests: install
	pytest --cov=${repo} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}
