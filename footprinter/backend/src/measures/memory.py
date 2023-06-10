"""
memory.py

This module provides a function to retrieve the total system memory.

Author: TheBoatyMcBoatFace
"""

import psutil
import sys
from pathlib import Path

# Add the project root directory to the module search path
sys.path.append(str(Path(__file__).resolve().parents[4]))

from footprinter.backend.src.utils.logger import logger


def get_system_memory():
    """
    Get the total system memory in gigabytes.

    Returns:
        float: The total system memory in gigabytes.
    """
    total_memory = psutil.virtual_memory().total
    memory_gb = total_memory / (1024 ** 3)

    logger.info(f"[bold dodger_blue2]Total System Memory:[/bold dodger_blue2] [steel_blue]{memory_gb:.2f} GB[/steel_blue]")

    return memory_gb


# Call the function to get total system memory
get_system_memory()
