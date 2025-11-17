from loguru import logger
import sys

# Remove default handler to avoid duplicates
logger.remove()

# Add console handler
logger.add(sys.stdout, level="DEBUG", format="<green>{time}</green> | <level>{level}</level> | <cyan>{message}</cyan>")

# Add file handler
logger.add("logs/app.log", rotation="1 MB", retention="10 days", level="INFO", encoding="utf-8")

__all__ = ["logger"]

