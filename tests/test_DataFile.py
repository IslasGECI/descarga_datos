import json

from descarga_datos import DataFile

TEXTO_ANALYSIS = """{
    "source": "datapackage",
    "path": "roedores_capturarecaptura_cedros",
    "filename": "roedores_capturarecaptura_cedros.csv",
    "version": "d2ca5a04850b",
    "type": "datapackage"
}"""


analisis: dict = json.loads(TEXTO_ANALYSIS)
datafile = DataFile(**analisis)


def test_datafile_filename_is_property():
    assert datafile.filename == "roedores_capturarecaptura_cedros.csv"


def test_analysis_name():
    assert datafile.path == "roedores_capturarecaptura_cedros"
