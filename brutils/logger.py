"""
Custom colored logger using built-in lib
Usage: from brutils.logger import logger

logger.info("This is an info message")
"""

import logging


class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[41m",  # Red background
    }
    RESET = "\033[0m"

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        message = super().format(record)
        return f"{color}{message}{self.RESET}"


logger = logging.getLogger("BR_Utils_Logger")
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = ColoredFormatter(
        "[%(name)s - %(levelname)s] %(asctime)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
