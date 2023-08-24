import logging
import click
# logging.basicConfig(level=logging.INFO, format='%(asctime)s == %(process)d == %(levelname)s: %(message)s', datefmt='%m/%d/%Y :: %I:%M:%S %p')
#
# logging.info("INFO")
# logging.debug("DEBUG")
# logging.warning("WARNING")
# logging.error("ERROR")
# logging.critical("CRITICAL")

@click.command
@click.option("--log_path")
def log_to_file(log_path):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s == %(process)d == %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y :: %I:%M:%S %p',
                        filename=log_path,
                        filemode="a")

    logging.info("INFO")
    logging.debug("DEBUG")
    logging.warning("WARNING")
    logging.error("ERROR")
    logging.critical("CRITICAL")

if __name__ == "__main__":
    log_to_file()


