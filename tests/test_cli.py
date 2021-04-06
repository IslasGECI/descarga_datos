from descarga_datos.cli import descarga_archivo, cli
import json
import os
import sys




TEXTO_ANALYSIS = """[
    {
        "docker_parent_image": "islasgeci/jupyter:5b83",
        "name": "Densidad de madrigueras de mérgulo a partir de busquedas exhaustivas",
        "description": "Mapas de densidad de madrigueras de mérgulo en Isla Guadalupe durante las temporadas 2014-2018.",
        "report": "mapa_densidad_censo.pdf",
        "results": [
            "densidad_mergulo_2014_morro_prieto.png"
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
            }
        ],
        "requirements": []
    },
    {
        "docker_parent_image": "islasgeci/jupyter:5b83",
        "name": "Resumen de esfuerzo de trampeo del periodo de abril a octubre del 2020",
        "description": "Muestra el resumen de esfuerzo total de abril a octubre del 2020",
        "report": "resumen_esfuerzo_erradicacion_gatos.pdf",
        "results": [
            "annual_captures_by_sex.csv"
        ],
        "scripts": [
            "src/plot_annual_pie_chart"
        ],
        "data": [
            {
                "source": "tabular_data_packages",
                "version": "1162b17368042ff665b534d61582e1a4b7a6e6fe",
                "path": "camaras_trampa_gatos_isla_guadalupe",
                "type": "json",
                "filename": "datapackage.json"
            }
        ],
        "requirements": []
    }
]"""

if not os.path.exists("./results"):
    os.mkdir("./results")

def test_descarga_archivo():
    archivo_existe = os.path.isfile("./analyses.json")
    if not archivo_existe:
        with open("analyses.json", "w") as archivo_salida:
            archivo_salida.write(TEXTO_ANALYSIS)
            archivo_salida.close()
    descarga_archivo(".", "./results", "camaras_trampa_gatos_isla_guadalupe")


def test_descarga_2_datapackage():
    os.system("descarga_datos datapackage.json ./results camaras_trampa_gatos_isla_guadalupe")
    assert os.path.isfile("./results/datapackage.json")
    with open("./results/datapackage.json", "r") as read_file:
        diccionario_analysis = json.load(read_file)    
    assert diccionario_analysis["name"] == "camaras_trampa_gatos_isla_guadalupe_2018_2021"
    os.system("descarga_datos datapackage.json ./results nidos_busqueda_aves_marinas")
    with open("./results/datapackage.json", "r") as read_file:
        diccionario_analysis = json.load(read_file)    
    assert diccionario_analysis["name"] == "nidos_busqueda_avesmarinas_todasislas"

def test_cli():
    sys.argv = ["cli.py", ".", "./results", "camaras_trampa_gatos_isla_guadalupe"]
    cli()
