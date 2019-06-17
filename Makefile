# Variable que guarda el nombre del paquete
nombreRepositorio := $(notdir $(CURDIR))
# Vairable que contiene la lista de pruebas del paquete
pruebasModulo := $(basename $(notdir $(wildcard $(nombreRepositorio)/tests/test_*.py)))

# Esta sección corre las pruebas
tests:
	docker build --tag $(nombreRepositorio) .
	docker run --interactive --tty --env BITBUCKET_USERNAME=${BITBUCKET_USERNAME} --env BITBUCKET_PASSWORD=${BITBUCKET_PASSWORD} $(nombreRepositorio) bash -c "pip install . && $(foreach script, $(pruebasModulo), python -m $(nombreRepositorio).tests.$(script) -v; )"
