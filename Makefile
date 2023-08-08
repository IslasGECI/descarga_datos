all: mutants

repo = descarga_datos
codecov_token = ed02def2-1ad1-4e23-81cc-0ede5dac22a7

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-repo-docstring \
        ${1}
endef

.PHONY: all clean format init linter mutants setup tests

check:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests

clean:
	rm --force --recursive .pytest_cache
	rm --force --recursive ${repo}.egg-info
	rm --force --recursive ${repo}/__pycache__
	rm --force --recursive ${repo}/**/__pycache__
	rm --force --recursive results
	rm --force --recursive test/__pycache__
	rm --force .coverage
	rm --force .mutmut-cache
	rm --force analyses.json

format:
	black --line-length 100 ${repo}
	black --line-length 100 tests

init: setup tests
	git config --global --add safe.directory /workdir
	git config --global user.name "Ciencia de Datos • GECI"
	git config --global user.email "ciencia.datos@islas.org.mx"

setup: clean install

install:
	pip install --editable .

linter:
	$(call lint, ${repo})
	$(call lint, tests)

mutants: setup
	mutmut run --paths-to-mutate ${repo}

tests:
	pytest --verbose


coverage: setup
	pytest --cov=${repo} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

red: format
	pytest --verbose \
	&& git restore tests/*.py \
	|| (git add tests/*.py && git commit -m "🛑🧪 Fail tests")
	chmod g+w -R .

green: format
	pytest --verbose \
	&& (git add ${repo}/*/*.py ${repo}/*.py tests/*.py && git commit -m "✅ Pass tests") \
	|| git restore ${repo}/*/*.py ${repo}/*.py
	chmod g+w -R .

refactor: format
	pytest --verbose \
	&& (git add ${repo}/*.py ${repo}/*/*.py tests/*.py && git commit -m "♻️  Refactor") \
	|| git restore ${repo}/*.py ${repo}/*/*.py tests/*.py
	chmod g+w -R .
