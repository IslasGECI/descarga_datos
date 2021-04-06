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
        },
        {
            "source": "tabular_data_packages",
            "version": "1162b173",
            "path": "camaras_trampa_gatos_isla_guadalupe",
            "type": "json",
            "filename": "datapackage.json"
        }

    ],
    "requirements": []
},
{
    "docker_parent_image": "islasgeci/jupyter:5b83",
    "name": "Densidad de madrigueras de mérgulo a partir de busquedas exhaustivas",
    "description": "Mapas de densidad de madrigueras de mérgulo en Isla Guadalupe durante las temporadas 2014-2018.",
    "report": "mapa_densidad_censo.pdf",
    "results": [
        "densidad_mergulo_todas_temporadas_zapato.png"
    ],
    "scripts": [
        "src/plot_burrows_density_map"
    ],
    "data": [
        {
            "source": "tabular_data_packages",
            "version": "b205951ba7d1720891edc9645cf5eceb669fdda6",
            "path": "nidos_busqueda_aves_marinas",
            "type": "json",
            "filename": "datapackage.json"
        },
        {
            "source": "archivos_binarios",
            "version": "d60fea2117a3c2f23be256ff34c112e1a2bd957c",
            "path": "shp/guadalupe",
            "type": "datapackage",
            "filename": "linea_costa_isla_guadalupe.shp"
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


def test_get_url_to_datafile_two_paths():
    expected_url = (
        "https://bitbucket.org/IslasGECI/tabular_data_packages/raw/1162b173/"
        + "camaras_trampa_gatos_isla_guadalupe/datapackage.json"
    )
    obtained_url = analisis.get_url_to_datafile("datapackage.json")
    assert obtained_url == (expected_url)
    expected_url = (
        "https://bitbucket.org/IslasGECI/tabular_data_packages/raw/d60fea2117/"
        + "nidos_busqueda_aves_marinas/datapackage.json"
    )
    obtained_url = analisis.get_url_to_datafile("datapackage.json")
    assert obtained_url == (expected_url)


def test_init():
    expected_description = (
        "Cantidad de individuos por transecto con captura y recaptura en Isla Cedros"
    )
    obtained_description = analisis._description
    assert obtained_description == expected_description
    obtained_docker_image = analisis._docker_parent_image
    expected_docker_image = "islasgeci/extension:d25d"
    assert obtained_docker_image == expected_docker_image
    assert analisis._report == ""
    assert analisis._results == []
    assert analisis._scripts == []
