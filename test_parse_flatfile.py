import unittest
from parse_flatfile import parse_flatfile


class TestParseFlatFile(unittest.TestCase):
    def test_parse_flatfile(self):
        """
        Test parse_flatfile() from parse_flatfile
        """
        # Files do not exists
        self.assertRaises(FileNotFoundError, parse_flatfile,
                          'not_exists_file', 'specs/testformat1.csv')
        self.assertRaises(FileNotFoundError, parse_flatfile,
                          'data/testformat1_2015-06-28.txt', 'not_exists_file')
        self.assertRaises(FileNotFoundError, parse_flatfile,
                          'not_exists_file', 'not_exists_file')

        # Success case
        self.assertEqual(parse_flatfile(
            'data/testformat1_2015-06-28.txt', 'specs/testformat1.csv'),
            [{'name': 'Foonyor', 'valid': True, 'count': 1},
             {'name': 'Barzane', 'valid': False, 'count': -12},
             {'name': 'Quuxitude', 'valid': True, 'count': 103}])

        # CSV header is not as required / Column(s) is (are) missing
        self.assertRaises(KeyError, parse_flatfile,
                          'data/testformat5_2015-06-28.txt', 'specs/testformat5.csv')

        # spec['width'] is not an integer
        self.assertRaises(ValueError, parse_flatfile,
                          'data/testformat6_2015-06-28.txt', 'specs/testformat6.csv')

        # spec['datatype'] is neither 'TEXT', 'BOOLEAN', nor 'INTEGER'
        self.assertRaises(ValueError, parse_flatfile,
                          'data/testformat7_2015-06-28.txt', 'specs/testformat7.csv')

        # Lines in data have inconsistent length with the specs
        self.assertRaises(ValueError, parse_flatfile,
                          'data/testformat2_2015-06-28.txt', 'specs/testformat2.csv')

        # Columns in data with BOOLEAN type are neither 1 or 0
        self.assertRaises(ValueError, parse_flatfile,
                          'data/testformat3_2015-06-28.txt', 'specs/testformat3.csv')

        # Columns in data with INTEGER type are not integers
        self.assertRaises(ValueError, parse_flatfile,
                          'data/testformat4_2015-06-28.txt', 'specs/testformat4.csv')

        # spec['width'] is smaller than 0
        self.assertRaises(ValueError, parse_flatfile,
                          'data/testformat8_2015-06-28.txt', 'specs/testformat8.csv')

        # spec['width'] is not 1 while spec['datatype'] is 'BOOLEAN'
        self.assertRaises(ValueError, parse_flatfile,
                          'data/testformat9_2015-06-28.txt', 'specs/testformat9.csv')


if __name__ == '__main__':
    unittest.main()
