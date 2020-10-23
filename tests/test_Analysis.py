import json

from descarga_datos import Analysis

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
            "version": "d2ca5a04850b",
            "type": "datapackage"
        }
    ],
    "requirements": []
}]"""


diccionario_analysis = json.loads(TEXTO_ANALYSIS)
analisis = diccionario_analysis[0]
analisis = Analysis(**analisis)


def test_datafile_name():
    obtained_filename = analisis._data[0].filename
    expected_filename = "roedores_capturarecaptura_cedros.csv"
    assert obtained_filename == expected_filename


def test_analysis_name():
    obtained_name = analisis.name
    expected_name = "Cantidad de individuos por transecto con captura y recaptura"
    assert obtained_name == expected_name


def test_is_dependent_on_datafile():
    assert analisis.is_dependent_on_datafile("roedores_capturarecaptura_cedros.csv")
    assert not analisis.is_dependent_on_datafile("rodores_capturarecaptura_cedros.csv")


def test_get_url_to_datafile():
    expected_url = (
        "https://bitbucket.org/IslasGECI/datapackage/raw/d2ca5a04850b/"
        + "roedores_capturarecaptura_cedros/roedores_capturarecaptura_cedros.csv"
    )
    obtained_url = analisis.get_url_to_datafile("roedores_capturarecaptura_cedros.csv")
    assert obtained_url == (expected_url)
    assert analisis.get_url_to_datafile("rodores_capturarecaptura_cedros.csv") is None


def test_init():
    expected_description = "Cantidad de individuos por transecto con captura y recaptura en Isla Cedros"
    obtained_description = analisis._description
    assert (
        obtained_description
        == expected_description
    )
    obtained_docker_image = analisis._docker_parent_image
    expected_docker_image = "islasgeci/extension:d25d"
    assert obtained_docker_image == expected_docker_image
    assert analisis._report == ""
    assert analisis._results == []
    assert analisis._scripts == []
