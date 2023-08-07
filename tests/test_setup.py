from typer.testing import CliRunner

from descarga_datos.setup_data import app

runner = CliRunner()


def test_setup_cli():
    file_to_download = "nidos_busqueda_aves_marinas.csv"
    destination_folder = "./results"
    tdp_path = "nidos_busqueda_aves_marinas"
    os.system(f"descarga_datos {file_to_download} {destination_folder} {tdp_path}")

    result = runner.invoke(app, ["--file-data-name", destination_folder + "/" + file_to_download])
    assert result.exit_code == 0
