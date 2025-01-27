import os
import unittest
import json
import jc.parsers.xml

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTests(unittest.TestCase):

    # input
    with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/generic/xml-cd_catalog.xml'), 'r', encoding='utf-8') as f:
        generic_xml_cd_catalog = f.read()

    with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/generic/xml-foodmenu.xml'), 'r', encoding='utf-8') as f:
        generic_xml_foodmenu = f.read()

    with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/generic/xml-nmap.xml'), 'r', encoding='utf-8') as f:
        generic_xml_nmap = f.read()

    # output
    with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/generic/xml-cd_catalog.json'), 'r', encoding='utf-8') as f:
        generic_xml_cd_catalog_json = json.loads(f.read())

    with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/generic/xml-foodmenu.json'), 'r', encoding='utf-8') as f:
        generic_xml_foodmenu_json = json.loads(f.read())

    with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/generic/xml-nmap.json'), 'r', encoding='utf-8') as f:
        generic_xml_nmap_json = json.loads(f.read())

    with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/generic/xml-nmap-raw.json'), 'r', encoding='utf-8') as f:
        generic_xml_nmap_r_json = json.loads(f.read())


    def test_xml_nodata(self):
        """
        Test xml parser with no data
        """
        self.assertEqual(jc.parsers.xml.parse('', quiet=True), [])

    def test_xml_nodata_r(self):
        """
        Test xml parser with no data and raw output
        """
        self.assertEqual(jc.parsers.xml.parse('', raw=True, quiet=True), [])

    def test_xml_cd_catalog(self):
        """
        Test the cd catalog xml file
        """
        self.assertEqual(jc.parsers.xml.parse(self.generic_xml_cd_catalog, quiet=True), self.generic_xml_cd_catalog_json)

    def test_xml_foodmenu(self):
        """
        Test the food menu xml file
        """
        self.assertEqual(jc.parsers.xml.parse(self.generic_xml_foodmenu, quiet=True), self.generic_xml_foodmenu_json)

    def test_xml_nmap(self):
        """
        Test nmap xml output
        """
        self.assertEqual(jc.parsers.xml.parse(self.generic_xml_nmap, quiet=True), self.generic_xml_nmap_json)

    def test_xml_nmap_r(self):
        """
        Test nmap xml raw output
        """
        self.assertEqual(jc.parsers.xml.parse(self.generic_xml_nmap, raw=True, quiet=True), self.generic_xml_nmap_r_json)


if __name__ == '__main__':
    unittest.main()
