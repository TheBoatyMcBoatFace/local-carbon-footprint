import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Append the parent directory to the sys path to import the cpu module correctly
sys.path.append(os.path.abspath('..'))

from footprinter.backend.src.measures import cpu


class CpuTest(unittest.TestCase):
    """
    Unit tests for the cpu module.
    """

    @patch('footprinter.backend.src.measures.cpu.psutil.cpu_percent')
    def test_get_cpu_utilization(self, mock_cpu_percent):
        """
        Test the get_cpu_utilization function.

        This method tests the CPU utilization value returned by the get_cpu_utilization function.
        It mocks the psutil.cpu_percent function to control the returned value.

        Args:
            mock_cpu_percent (MagicMock): Mock object for the psutil.cpu_percent function.
        """
        # Mock the cpu_percent function to return a specific value
        mock_cpu_percent.return_value = 75.0

        # Call the function to get the CPU utilization
        utilization = cpu.get_cpu_utilization()

        # Assert that the utilization is within the expected range
        self.assertGreaterEqual(utilization, 0.0)
        self.assertLessEqual(utilization, 100.0)

    @patch('footprinter.backend.src.measures.cpu.logger')
    @patch('footprinter.backend.src.measures.cpu.psutil.cpu_percent')
    def test_logging(self, mock_cpu_percent, mock_logger):
        """
        Test the logging in the cpu module.

        This method tests that the appropriate log message is logged when calling the get_cpu_utilization function.

        Args:
            mock_cpu_percent (MagicMock): Mock object for the psutil.cpu_percent function.
            mock_logger (MagicMock): Mock object for the logger module.
        """
        # Mock the cpu_percent function to return a specific value
        mock_cpu_percent.return_value = 75.0

        # Call the function to get the CPU utilization
        cpu.get_cpu_utilization()

        # Assert that the log message is logged at the appropriate log level
        mock_logger.info.assert_called_with('[bold dodger_blue2]CPU Utilization:[/bold dodger_blue2] [steel_blue]75.0%[/steel_blue]')


if __name__ == '__main__':
    unittest.main()
