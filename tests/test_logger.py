import unittest
from unittest.mock import patch, MagicMock
import time
import logging
from footprinter import logger


class LoggerTest(unittest.TestCase):

    def test_logger_output(self):
        with patch('footprinter.logger.time', MagicMock(wraps=time)) as mock_time:
            # Set the mock time to a specific value
            mock_time.strftime.return_value = '2023-06-09'

            # Create a stream handler to capture the log output
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            log_output = []

            def capture_logs(record):
                log_output.append(record.getMessage())

            stream_handler.setFormatter(logging.Formatter('%(message)s'))
            stream_handler.emit = capture_logs

            # Add the stream handler to the logger
            logger.addHandler(stream_handler)

            # Log some messages
            logger.debug('This is a debug message')
            logger.info('This is an info message')
            logger.warning('This is a warning message')
            logger.error('This is an error message')
            logger.critical('This is a critical message')

            # Assert the captured log messages
            expected_output = [
                'This is a debug message',
                'This is an info message',
                'This is a warning message',
                'This is an error message',
                'This is a critical message'
            ]
            self.assertEqual(log_output, expected_output)

            # Remove the stream handler from the logger
            logger.removeHandler(stream_handler)


if __name__ == '__main__':
    unittest.main()
