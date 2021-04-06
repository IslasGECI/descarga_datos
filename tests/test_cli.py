from descarga_datos.cli import descarga_archivo, cli
import sys
import os.path


TEXTO_ANALYSIS = """[{
    "name": "Cantidad de individuos por transecto con captura y recaptura",
    "description": "Cantidad de individuos por transecto con captura y recaptura en Isla Cedros",
    "docker_parent_image": "islasgeci/extension:d25d",
    "report": "",
    "results": [
    ],
    "scripts": [
    ],
    "data": [
        {
            "source": "datapackage",
            "path": "roedores_capturarecaptura_cedros",
            "filename": "roedores_capturarecaptura_cedros.csv",
            "version": "xxxx",
            "type": "datapackage"
        }
    ],
    "requirements": []
}]"""


def test_descarga_archivo():
    archivo_existe = os.path.isfile("./analyses.json")
    if not archivo_existe:
        with open("analyses.json", "w") as archivo_salida:
            archivo_salida.write(TEXTO_ANALYSIS)
            archivo_salida.close()
    descarga_archivo(".", "./results")


def test_cli():
    sys.argv = ["cli.py", ".", "./results"]
    cli()
