import descarga_datos
from descarga_datos import download_file_from_repo
from descarga_datos.utils import (
    get_password_from_enviormet_variable,
    get_user_from_enviorment_variable,
)


def test_download_file_from_repo():
    archivo = descarga_datos.internals.DataFile(
        "tabular_data_packages",
        "esfuerzos_capturas_gatos_socorro",
        "captura_gatos_socorro.csv",
        "a3e8",
        "csv",
    )
    url = archivo.get_url_to_file()
    destination_folder = "./"
    download_file_from_repo(
        url,
        destination_folder,
        get_user_from_enviorment_variable(),
        get_password_from_enviormet_variable(),
    )
