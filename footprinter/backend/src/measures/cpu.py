"""
cpu.py

This module provides functions to retrieve CPU utilization information.

Author: TheBoatyMcBoatFace
"""

import psutil
import sys
from pathlib import Path

# Add the project root directory to the module search path
sys.path.append(str(Path(__file__).resolve().parents[4]))

from footprinter.backend.src.utils.logger import logger


def get_cpu_utilization():
    """
    Get the current CPU utilization.

    Returns:
        float: The CPU utilization as a percentage.
    """
    utilization = psutil.cpu_percent()
    logger.info(f'[bold dodger_blue2]CPU Utilization:[/bold dodger_blue2] [steel_blue]{utilization}%[/steel_blue]')
    return utilization


# Call the function to get CPU utilization
get_cpu_utilization()
