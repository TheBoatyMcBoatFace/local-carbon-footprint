import unittest
from unittest.mock import patch, MagicMock
from footprinter.backend.src.measures.memory import get_system_memory


class MemoryTest(unittest.TestCase):

    @patch('footprinter.backend.src.measures.memory.psutil.virtual_memory')
    def test_get_system_memory(self, mock_virtual_memory):
        mock_total_memory = 1024 * 1024 * 1024  # 1 GB
        mock_virtual_memory.return_value.total = mock_total_memory

        memory_gb = get_system_memory()

        # Assert the returned memory in gigabytes
        expected_memory_gb = 1.0
        self.assertEqual(memory_gb, expected_memory_gb)


if __name__ == '__main__':
    unittest.main()
