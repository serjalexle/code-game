from loguru import logger
import sys

# Remove default logger to avoid duplication
logger.remove()

# Add custom logger for console
logger.add(
    sink=sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
    level="DEBUG",
)

# Add custom logger for file
logger.add(
    "app.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
    level="INFO",
    rotation="10 MB",  # Rotate log file after 1 MB
    compression="zip",  # Compress old log files
)

# Export the logger for use in other modules
__all__ = ["logger"]
