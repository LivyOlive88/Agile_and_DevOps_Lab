"""
logger.py - Centralized Logging Configuration

This module provides a centralized logging setup for the entire
data analysis pipeline. All other modules import the configured
logger from here to ensure consistent log formatting.
"""

import logging


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Create and configure a logger with a standard format.

    Parameters
    ----------
    name : str
        Name of the logger (typically __name__ of the calling module).
    level : int
        Logging level (default: logging.INFO).

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if logger already has one
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
