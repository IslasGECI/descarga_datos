all: mutants

repo = descarga_datos
codecov_token = ed02def2-1ad1-4e23-81cc-0ede5dac22a7

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

.PHONY: all clean format install linter mutants tests

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

linter:
	$(call lint, ${repo})
	$(call lint, tests)

mutants:
	mutmut run --paths-to-mutate ${repo}

tests: install
	pytest --cov=${repo} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}
