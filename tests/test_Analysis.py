import json

from descarga_datos import Analysis

TEXTO_ANALYSIS = """[
    {
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
    }
]"""


diccionario_analysis = json.loads(TEXTO_ANALYSIS)
analisis = diccionario_analysis[0]
analisis = Analysis(**analisis)


def test_datafile_name():
    assert analisis._data[0].filename == "roedores_capturarecaptura_cedros.csv"


def test_analysis_name():
    assert analisis.name == "Cantidad de individuos por transecto con captura y recaptura"


def test_is_dependent_on_datafile():
    assert analisis.is_dependent_on_datafile("roedores_capturarecaptura_cedros.csv")
    assert not analisis.is_dependent_on_datafile("rodores_capturarecaptura_cedros.csv")


def test_get_url_to_datafile():
    assert (
        analisis.get_url_to_datafile("roedores_capturarecaptura_cedros.csv")
        == "https://bitbucket.org/IslasGECI/datapackage/raw/d2ca5a04850b/"
        + "roedores_capturarecaptura_cedros/roedores_capturarecaptura_cedros.csv",
    )
    assert analisis.get_url_to_datafile("rodores_capturarecaptura_cedros.csv") is None


def test_init():
    assert (
        analisis._description
        == "Cantidad de individuos por transecto con captura y recaptura en Isla Cedros"
    )
    assert analisis._docker_parent_image == "islasgeci/extension:d25d"
    assert analisis._report == ""
    assert analisis._results == []
    assert analisis._scripts == []
