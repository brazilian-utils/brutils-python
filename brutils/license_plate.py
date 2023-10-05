def remove_symbols(license_plate_number: str):  # type: (str) -> str
    """Removes the dash (-) symbol from a license plate string.

    Args:
                    license_plate_number[str]: A license plate string
    Returns:
                    [str]: A license plate string without symbols
    """
    return license_plate_number.replace("-", "")
