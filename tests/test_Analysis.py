import json

from descarga_datos import Analysis

TEXTO_ANALYSIS = """[{
    "name": "Cantidad de individuos por transecto con captura y recaptura",
    "description": "Cantidad de individuos por transecto con captura y recaptura en Isla Cedros",
    "image_tag": "d52d",
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
        },
        {
            "source": "tabular_data_packages",
            "version": "1162b173",
            "path": "camaras_trampa_gatos_isla_guadalupe",
            "type": "json",
            "filename": "datapackage.json"
        },
        {
            "source": "archivos_binarios",
            "version": "d60fea211",
            "path": "shp/guadalupe",
            "type": "datapackage",
            "filename": "datapackage.json"
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
    assert analisis.is_dependent_on_datafile(
        "roedores_capturarecaptura_cedros", "roedores_capturarecaptura_cedros.csv"
    )
    assert not analisis.is_dependent_on_datafile(
        "roedores_capturarecaptura_cedros", "rodores_capturarecaptura_cedros.csv"
    )


def assert_get_url_to_datafile(dictionary):
    expected_url = (
        f"https://bitbucket.org/IslasGECI/{dictionary['source']}/raw/{dictionary['version']}/"
        + f"{dictionary['path']}/{dictionary['filename']}"
    )
    obtained_url = analisis.get_url_to_datafile(dictionary["path"], dictionary["filename"])
    assert obtained_url == expected_url


def test_get_url_to_datafile():
    datafile = {
        "source": "datapackage",
        "path": "roedores_capturarecaptura_cedros",
        "filename": "roedores_capturarecaptura_cedros.csv",
        "version": "d2ca5a04850b",
        "type": "datapackage",
    }
    assert_get_url_to_datafile(datafile)
    assert (
        analisis.get_url_to_datafile(
            "roedores_capturarecaptura_cedros", "rodores_capturarecaptura_cedros.csv"
        )
        is None
    )


def test_get_url_to_datafile_two_paths():
    first_datafile = {
        "source": "archivos_binarios",
        "version": "d60fea211",
        "path": "shp/guadalupe",
        "type": "datapackage",
        "filename": "datapackage.json",
    }
    assert_get_url_to_datafile(first_datafile)
    second_datafile = {
        "source": "tabular_data_packages",
        "version": "1162b173",
        "path": "camaras_trampa_gatos_isla_guadalupe",
        "type": "json",
        "filename": "datapackage.json",
    }
    assert_get_url_to_datafile(second_datafile)


def test_init():
    expected_description = (
        "Cantidad de individuos por transecto con captura y recaptura en Isla Cedros"
    )
    obtained_description = analisis._description
    assert obtained_description == expected_description
    obtained_image_tag = analisis._image_tag
    expected_image_tag = "d52d"
    assert obtained_image_tag == expected_image_tag
    assert analisis._report == ""
    assert analisis._results == []
    assert analisis._scripts == []
