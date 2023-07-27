"""
geo.py

This module provides functions to retrieve geolocation information.

Author: TheBoatyMcBoatFace
"""

import requests
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table

# Add the project root directory to the module search path
sys.path.append(str(Path(__file__).resolve().parents[4]))

from footprinter.backend.src.utils.logger import logger


def get_location_table():
    """
    Get the geolocation information in a table format.

    Returns:
        rich.table.Table: The geolocation information as a Rich table.
    """
    logger.debug('Getting Location')
    response = requests.get('http://ip-api.com/json/')
    geodata = response.json()

    table = Table(title="Geolocation")
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    keys = ['query', 'continent', 'country', 'region', 'city', 'district', 'zip', 'lat', 'lon', 'timezone', 'isp', 'org']

    for key in keys:
        if key in geodata:
            value = str(geodata[key])
        else:
            value = "N/A"
        table.add_row(key.capitalize(), value)

    return table


def get_location():
    """
    Get the country and region of the current location.

    Returns:
        tuple: A tuple containing the country and region strings.
    """
    logger.debug('Getting Location')
    response = requests.get('http://ip-api.com/json/')
    geodata = response.json()
    country = geodata['country']
    region = geodata['region']

    return country, region


# Check if the script is run directly
if __name__ == '__main__':
    country, region = get_location()
    logger.info(f"[bold cyan]Country:[/bold cyan] [steel_blue]{country}[/steel_blue]")
    logger.info(f"[bold cyan]Region:[/bold cyan] [steel_blue]{region}[/steel_blue]")
