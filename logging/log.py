import logging


# logging.basicConfig(level=logging.DEBUG)

# logging.debug("This is a debug message")     # Detailed debugging info
# logging.info("This is an info message")      # General info
# logging.warning("This is a warning message") # Something unexpected
# logging.error("This is an error message")    # Error occurred
# logging.critical("This is critical!")        # Serious issue


#logging into a file
logging.basicConfig(
    filename="app.log",         # log file name
    filemode="a",               # append mode
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error has occurred")