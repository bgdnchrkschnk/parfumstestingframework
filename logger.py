import logging
import os.path

import click


#### BASE_CLI LOGGER: ######

# logging.basicConfig(level=logging.INFO, format='%(asctime)s == %(process)d == %(levelname)s: %(message)s', datefmt='%m/%d/%Y :: %I:%M:%S %p')
#
# logging.info("INFO")
# logging.debug("DEBUG")
# logging.warning("WARNING")
# logging.error("ERROR")
# logging.critical("CRITICAL")

#### BASE_FILE LOGGER: ######

# @click.command
# @click.option("--log_path")
# def log_to_file(log_path):
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s == %(process)d == %(levelname)s: %(message)s',
#                         datefmt='%m/%d/%Y :: %I:%M:%S %p',
#                         filename=log_path,
#                         filemode="a")
#
#     logging.info("INFO")
#     logging.debug("DEBUG")
#     logging.warning("WARNING")
#     logging.error("ERROR")
#     logging.critical("CRITICAL")
#
# if __name__ == "__main__":
#     log_to_file()

#### CUSTOMER LOGGER: ######
@click.command
@click.option("--log_path")
def to_log(log_path):
    custom_logger = logging.getLogger(__file__)

    # Creating handlers for console and file logging, setlevels for them
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    f_handler = logging.FileHandler(log_path)
    f_handler.setLevel(logging.INFO)

    # Create formatters for each handler
    c_handler_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    f_handler_format = logging.Formatter('%(asctime)s == %(process)d == %(name)s == %(levelname)s: %(message)s')

    # Set formatters for handlers
    c_handler.setFormatter(c_handler_format)
    f_handler.setFormatter(f_handler_format)

    # Add handlers to our logger objects
    custom_logger.addHandler(c_handler)
    custom_logger.addHandler(f_handler)

    custom_logger.info("I am info log message")
    custom_logger.debug("I am debug log message")
    custom_logger.warning("I am warning log message")
    custom_logger.error("I am error log message")
    custom_logger.critical("I am error log message")


if __name__ == '__main__':
    to_log()
