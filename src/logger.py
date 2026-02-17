"""
logger.py - Centralized Logging Configuration

This module provides a centralized logging setup for the entire
data analysis pipeline. All other modules import the configured
logger from here to ensure consistent log formatting.
Logs are output to both the console and a log file.
"""

import os
import logging


LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
LOG_FILE = os.path.join(LOG_DIR, "pipeline.log")


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Create and configure a logger with console and file output.

    Parameters
    ----------
    name : str
        Name of the logger (typically __name__ of the calling module).
    level : int
        Logging level (default: logging.INFO).

    Returns
    -------
    logging.Logger
        Configured logger instance with console and file handlers.
    """
    # Create logs directory if it does not exist
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if logger already has them
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Console handler - prints logs to terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler - saves logs to pipeline.log
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
