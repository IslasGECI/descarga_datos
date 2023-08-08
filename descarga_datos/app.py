import typer

app = typer.Typer()


@app.command()
def setup_data(file_data_name: str = "", report: str = "", analysis: str = "analyses.json"):
    pass
