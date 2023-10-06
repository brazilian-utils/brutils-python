def remove_symbols(processo_juridico: str):  # type: (str) -> str
    """Removes common symbols from a legal process number string.
    The standard symbols removed are "." and "-"

    Args:
                    process_juridico[str]: A legal process number string
    Returns:
                    [str]: A legal process number string without symbols
    """
    return processo_juridico.replace(".", "").replace("-", "")
