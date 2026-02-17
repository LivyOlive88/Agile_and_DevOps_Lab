"""
monitor.py - Pipeline Monitoring Utilities

This module provides tools to monitor pipeline performance, including
execution time and resource usage tracking.

User Story: US-05 (Pipeline Monitoring & Logging)
"""

import time
import functools
import psutil
import os
from src.logger import setup_logger

logger = setup_logger(__name__)


def track_performance(func):
    """
    Decorator to track execution time and memory usage of a function.

    Parameters
    ----------
    func : callable
        The function to monitored.

    Returns
    -------
    callable
        The wrapped function with monitoring logic.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())

        # Record start state
        start_time = time.time()
        start_memory = process.memory_info().rss / (1024 * 1024)  # MB

        logger.info("Starting execution of '%s'", func.__name__)

        try:
            result = func(*args, **kwargs)

            # Record end state
            end_time = time.time()
            end_memory = process.memory_info().rss / (1024 * 1024)  # MB

            duration = end_time - start_time
            memory_change = end_memory - start_memory

            logger.info(
                "Completed '%s' in %.4f seconds. Memory Usage: %.2f MB (Change: %+.2f MB)",
                func.__name__, duration, end_memory, memory_change
            )
            return result

        except Exception as e:
            logger.error("Error in '%s': %s", func.__name__, e)
            raise e

    return wrapper
