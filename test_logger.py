"""
Simple test for the project logger.
"""

from src.logger import logger

logger.info("Logger initialized successfully.")

logger.warning("This is a sample warning.")

logger.error("This is a sample error.")

print("Logger test completed.")