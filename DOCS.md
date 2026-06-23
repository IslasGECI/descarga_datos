# Documentation

## `get_token_from_environment_variable() -> str`

Return the Bitbucket API token from the `BITBUCKET_API_TOKEN` environment variable.

- Returns: `str` — the API token value
- Errors: `KeyError` if `BITBUCKET_API_TOKEN` is not set

## `get_email_from_environment_variable() -> str`

Return the Bitbucket account email from the `BITBUCKET_EMAIL` environment variable.

- Returns: `str` — the email address
- Errors: `KeyError` if `BITBUCKET_EMAIL` is not set

## `DataFile(source, path, filename, version, type)`

Represents a data file specified as a dependency of an analysis in `analyses.json`.

Parameters:
- `source: str` — Name of the repository where the data is stored
- `path: str` — Path to the data inside the repository
- `filename: str` — Name of the data file
- `version: str` — Commit hash of the version where the data was committed
- `type: str` — Data type identifier (e.g. datapackage, gpx, csv, excel)

### `DataFile.filename -> str`

The name of the file.

### `DataFile.path -> str`

The path of the file within the repository.

### `DataFile.get_url_to_file() -> str`

Return the authenticated URL to download the file from Bitbucket.

- Returns: `str` — URL containing credentials for the Bitbucket REST API
- Notes: Credentials are read from `BITBUCKET_EMAIL` and `BITBUCKET_API_TOKEN` environment variables

## `download_file_from_repo(url: str, filename: str)`

Download a file from a Bitbucket repository to a local directory.

Parameters:
- `url: str` — Authenticated URL of the file in the Bitbucket repository
- `filename: str` — Local directory path where the downloaded file will be saved

## `Analysis(**data)`

Represents an analysis entry from `analyses.json`.

Parameters:
- `name: str` — Name of the analysis
- `description: str` — Description of the analysis
- `image_tag: str` — Docker image tag
- `docker_parent_image: str` — Parent Docker image (optional)
- `report: str` — Report filename
- `results: list` — Expected result filenames
- `scripts: list` — Script paths
- `data: list` — Data file dependency descriptors
- `requirements: list` — Package dependencies
- `setup_data: list` — Data setup configurations (optional)

### `Analysis.name -> str`

The name of the analysis.

### `Analysis.is_dependent_on_datafile(path: str, filename: str) -> bool`

Check whether this analysis depends on a specific data file.

- Returns: `True` if the analysis has a data dependency matching the given path and filename, `False` otherwise

### `Analysis.get_url_to_datafile(path: str, filename: str) -> str | None`

Return the download URL for a specific data file that this analysis depends on.

- Returns: `str` — authenticated download URL, or `None` if no matching data file is found

## CLI: `descarga_datos`

```
descarga_datos <filename> <destination_folder> <path>
```

Download data files specified in `analyses.json` that match the given path and filename.

- `filename: str` — Name of the file to download
- `destination_folder: str` — Local directory to save the downloaded file
- `path: str` — Path to the data inside the repository

## CLI: `setup_data`

```
setup_data <filename> <destination_folder> <path>
```

Download and prepare data files for analysis, applying column adaptations.
