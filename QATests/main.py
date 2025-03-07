from settings.loggers import logging


if __name__ == "__main__":
    logging.info("Starting the application")

    try:
        # Simulate some operation that might raise an exception
        result = 10 / 0
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    logging.warning("This some warning")
