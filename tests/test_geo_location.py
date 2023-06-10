import unittest
from unittest.mock import patch, MagicMock
from footprinter.backend.src.measures.geo import get_location_table, get_location


class GeoTest(unittest.TestCase):

    @patch('footprinter.backend.src.measures.geo.requests.get')
    def test_get_location(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'country': 'United States',
            'region': 'California'
        }
        mock_get.return_value = mock_response

        country, region = get_location()

        # Assert the returned country and region
        self.assertEqual(country, 'United States')
        self.assertEqual(region, 'California')


if __name__ == '__main__':
    unittest.main()
