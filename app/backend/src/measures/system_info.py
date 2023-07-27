"""
system_info.py

This module provides functions to retrieve system information such as machine name, machine type, and CPU info.

Author: TheBoatyMcBoatFace
"""

import platform
import sys
from pathlib import Path

# Add the project root directory to the module search path
sys.path.append(str(Path(__file__).resolve().parents[4]))

from footprinter.backend.src.utils.logger import logger


def get_machine_name():
    """
    Get the machine name.

    Returns:
        str: The machine name.
    """
    machine_name = platform.node()
    logger.info(f"[bold dodger_blue2]Machine Name:[/bold dodger_blue2] [steel_blue]{machine_name}[/steel_blue]")
    return machine_name


def get_machine_type():
    """
    Get the machine type.

    Returns:
        str: The machine type.
    """
    machine_type = platform.machine()
    logger.info(f"[bold dodger_blue2]Machine Type:[/bold dodger_blue2] [steel_blue]{machine_type}[/steel_blue]")
    return machine_type


def get_cpu_info():
    """
    Get the CPU info.

    Returns:
        str: The CPU info.
    """
    cpu_info = platform.processor()
    logger.info(f"[bold dodger_blue2]CPU Info:[/bold dodger_blue2] [steel_blue]{cpu_info}[/steel_blue]")
    return cpu_info


def get_system_info():
    """
    Get system information.

    Returns:
        dict: A dictionary containing various system-related metrics.
    """
    system_info = {
        "Machine Name": get_machine_name(),
        "Machine Type": get_machine_type(),
        "CPU Info": get_cpu_info(),
        # Add more system-related metrics here
    }
    return system_info


# Call the function to get system information
system_info = get_system_info()
for key, value in system_info.items():
    logger.info(f"{key}: {value}")
