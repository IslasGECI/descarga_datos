import json
import unittest

from descarga_datos import DataFile

TEXTO_ANALYSIS = """{
    "source": "datapackage",
    "path": "roedores_capturarecaptura_cedros",
    "filename": "roedores_capturarecaptura_cedros.csv",
    "version": "d2ca5a04850b",
    "type": "datapackage"
}"""


class TestDataFile(unittest.TestCase):

    def setUp(self):
        diccionario_analysis = json.loads(TEXTO_ANALYSIS)
        analisis = diccionario_analysis
        self.datafile = DataFile(**analisis)

    def test_datafile_filename_is_property(self):
        self.assertEqual(
            self.datafile.filename, "roedores_capturarecaptura_cedros.csv")

    def test_analysis_name(self):
        self.assertEqual(
            self.datafile.path, "roedores_capturarecaptura_cedros")


if __name__ == '__main__':
    unittest.main()
