"""
    VAG API

    Web-API für Echtzeitinformationen der VAG Nürnberg  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.vag.api.fahrten_api import FahrtenApi  # noqa: E501

from deutschland import vag


class TestFahrtenApi(unittest.TestCase):
    """FahrtenApi unit test stubs"""

    def setUp(self):
        self.api = FahrtenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fahrten_get(self):
        """Test case for fahrten_get

        Liefert alle laufenden und startenden Fahrten zu dem angegebenen Betriebszweig innerhalb des angegebenen Zeitfenster.  # noqa: E501
        """
        pass

    def test_fahrten_get_fahrt1(self):
        """Test case for fahrten_get_fahrt1

        Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem aktuellen Betriebstag  # noqa: E501
        """
        pass

    def test_fahrten_get_fahrt2(self):
        """Test case for fahrten_get_fahrt2

        Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem angegebenen Betriebstag  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()