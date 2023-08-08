from descarga_datos.app import app

import os
import pandas as pd
from typer.testing import CliRunner

runner = CliRunner()


def test_setup_cli():
    file_to_download = "nidos_busqueda_aves_marinas.csv"
    destination_folder = "./results"
    tdp_path = "nidos_busqueda_aves_marinas"
    os.system(f"descarga_datos {file_to_download} {destination_folder} {tdp_path}")

    data_path = destination_folder + "/" + file_to_download
    original_data = pd.read_csv(data_path)

    result = runner.invoke(
        app,
        [
            "--file-data-name",
            data_path,
            "--report",
            "tamanio_poblacional",
            "--analysis",
            "tests/data/analyses_tamanio.json",
        ],
    )
    assert result.exit_code == 0
    filtered_data = pd.read_csv(data_path)
    assert len(filtered_data) < len(original_data)
