from descarga_datos.cli import descarga_archivo, cli
import sys


def test_descarga_archivo():
    descarga_archivo(".", "./results")


def test_cli():
    sys.argv = ["cli.py", ".", "./results"]
    cli()
