from setuptools import setup, find_packages

setup(
    name="descarga_datos",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "descarga_datos = descarga_datos.cli:cli",
        ]
    },
)
