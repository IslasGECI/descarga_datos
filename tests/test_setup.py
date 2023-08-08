from descarga_datos.app import app

import os
import pandas as pd
from typer.testing import CliRunner

runner = CliRunner()


def test_setup_cli():
    data_path = "results/nidos_busqueda_aves_marinas_for_app.csv"
    os.system(f"cp tests/data/nidos_busqueda_aves_marinas.csv {data_path}")

    original_data = pd.read_csv(data_path)

    result = runner.invoke(
        app,
        [
            "--file-data-name",
            data_path,
            "--report",
            "tamano_poblacional.pdf",
            "--analysis",
            "tests/data/analyses_tamanio.json",
        ],
    )
    assert result.exit_code == 0
    filtered_data = pd.read_csv(data_path)
    assert len(filtered_data) < len(original_data)
    assert (filtered_data.columns == original_data.columns).all()
    os.remove(data_path)
