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
    obtained_filename = datafile.filename
    expected_filename = analisis["filename"]
    assert obtained_filename == expected_filename


def test_analysis_name():
    obtained_path = datafile.path
    expected_path = analisis["path"]
    assert obtained_path == expected_path


def test_init():
    obtained_source = datafile._source
    expected_source = analisis["source"]
    assert obtained_source == expected_source
    obtained_version = datafile._version
    expected_version = analisis["version"]
    assert obtained_version == expected_version
    obtained_type = datafile._type
    expected_type = analisis["type"]
    assert obtained_type == expected_type
