# descarga_datos

Download data files from Bitbucket repositories using the definitions in `analyses.json`.

## What it does

This tool reads an `analyses.json` file that describes which data files are needed for a set of analyses. It downloads each file from a Bitbucket repository and saves it locally so you can use it in your analysis pipeline.

## Before you start

You need:

- A Bitbucket account with access to the GECI repositories
- An [API token](https://bitbucket.org/account/settings/app-passwords/) with read permissions
- Your Atlassian account email address

Set these environment variables:

```bash
export BITBUCKET_EMAIL="your.email@example.com"
export BITBUCKET_API_TOKEN="your-api-token"
```

## Run the project

### With Docker (recommended)

```bash
docker compose build
docker compose run --rm islasgeci descarga_datos <filename> <destination_folder> <path>
```

### Without Docker

```bash
pip install git+https://github.com/IslasGECI/descarga_datos.git
descarga_datos <filename> <destination_folder> <path>
```

The tool reads `analyses.json` from the current directory and downloads matching files.
