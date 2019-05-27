from .DataFile import DataFile


class Analysis:
    def __init__(self, name: str, description: str, docker_parent_image: str,
                 report: str, results: list, scripts: list, data: list,
                 requirements: list):
        self._name = name
        self._description = description
        self._docker_parent_image = docker_parent_image
        self._report = report
        self._results = results
        self._scripts = scripts
        self._data = self._construct_datafile_array(data)

    def _construct_datafile_array(self, data):
        archivos_datos = []
        for datos in self._data:
            archivos_datos.append(DataFile(**datos))
        return archivos_datos

    @property
    def name(self):
        return self._name

    def depends_on_file(self, filename: str) -> bool:
        for archivo_datos in self._data:
            if archivo_datos.filename == filename:
                return True
        return False

    def get_url_to_file(self, filename: str):
        for archivo_datos in self._data:
            if archivo_datos.filename == filename:
                return archivo_datos.get_url_to_file()
        return None
