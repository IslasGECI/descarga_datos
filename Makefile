
all: README.pdf

nombreRepositorio := $(notdir $(CURDIR))
pruebasModulo := $(basename $(notdir $(wildcard $(nombreRepositorio)/tests/test_*.py)))

# Reglas para construir los objetivos principales
README.pdf: README.md # La fuente README.md debe estar en UTF-8 por el pandoc
	pandoc README.md -o README.pdf
	start "" /max "README.pdf"

# Esta sección corre las pruebas
tests:
	docker build --tag $(nombreRepositorio) .
	docker run --interactive --tty --env BITBUCKET_USERNAME=${BITBUCKET_USERNAME} --env BITBUCKET_PASSWORD=${BITBUCKET_PASSWORD} $(nombreRepositorio) bash -c "pip install . && $(foreach script, $(pruebasModulo), python -m $(nombreRepositorio).tests.$(script) -v; )"
