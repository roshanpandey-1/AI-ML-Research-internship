import logging

# Create logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# File handler
file_handler = logging.FileHandler("debug.log")
file_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example logs
logger.debug("Debugging info")
logger.info("Informational message")
logger.warning("Warning message")
