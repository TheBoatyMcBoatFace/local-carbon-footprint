import unittest
from unittest.mock import patch, MagicMock
from footprinter.backend.src.measures.system_info import get_machine_name, get_machine_type, get_cpu_info, get_system_info


class SystemInfoTest(unittest.TestCase):

    @patch('footprinter.backend.src.measures.system_info.platform.node')
    def test_get_machine_name(self, mock_node):
        mock_machine_name = "MyMachine"
        mock_node.return_value = mock_machine_name

        machine_name = get_machine_name()

        # Assert the returned machine name
        self.assertEqual(machine_name, mock_machine_name)

    @patch('footprinter.backend.src.measures.system_info.platform.machine')
    def test_get_machine_type(self, mock_machine):
        mock_machine_type = "x86_64"
        mock_machine.return_value = mock_machine_type

        machine_type = get_machine_type()

        # Assert the returned machine type
        self.assertEqual(machine_type, mock_machine_type)

    @patch('footprinter.backend.src.measures.system_info.platform.processor')
    def test_get_cpu_info(self, mock_processor):
        mock_cpu_info = "Intel Core i7"
        mock_processor.return_value = mock_cpu_info

        cpu_info = get_cpu_info()

        # Assert the returned CPU info
        self.assertEqual(cpu_info, mock_cpu_info)

    @patch('footprinter.backend.src.measures.system_info.get_machine_name')
    @patch('footprinter.backend.src.measures.system_info.get_machine_type')
    @patch('footprinter.backend.src.measures.system_info.get_cpu_info')
    def test_get_system_info(self, mock_get_cpu_info, mock_get_machine_type, mock_get_machine_name):
        mock_machine_name = "MyMachine"
        mock_machine_type = "x86_64"
        mock_cpu_info = "Intel Core i7"

        mock_get_machine_name.return_value = mock_machine_name
        mock_get_machine_type.return_value = mock_machine_type
        mock_get_cpu_info.return_value = mock_cpu_info

        system_info = get_system_info()

        # Assert the returned system information dictionary
        expected_system_info = {
            "Machine Name": mock_machine_name,
            "Machine Type": mock_machine_type,
            "CPU Info": mock_cpu_info,
        }
        self.assertEqual(system_info, expected_system_info)


if __name__ == '__main__':
    unittest.main()
