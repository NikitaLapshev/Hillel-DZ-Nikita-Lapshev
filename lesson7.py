import time
import logging

class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        logging.info(f"Блок выполнен за {elapsed_time:.0f} секунд")
        if exc_type:
            logging.error(f"Исключение {exc_type}: {exc_value}")
        return False



logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

with TimerContext():
    time.sleep(2)

# Global configuration representing application settings
GLOBAL_CONFIG = {
    "feature_a": True,
    "feature_b": False,
    "max_retries": 3
}


class Configuration:
    def __init__(self, updates, validator=None):
        """Context manager for temporarily modifying the global configuration."""
        self.updates = updates
        self.validator = validator
        self.original_config = None

    def __enter__(self):
        """
        Enter the context: Apply the configuration updates.
        """
        # Save a copy of the current GLOBAL_CONFIG
        self.original_config = GLOBAL_CONFIG.copy()
        logging.info("Original configuration saved: %s", self.original_config)

        # Apply updates
        GLOBAL_CONFIG.update(self.updates)
        logging.info("Applied updates to configuration: %s", self.updates)

        # Validate the updated configuration if a validator is provided
        if self.validator:
            is_valid = self.validator(GLOBAL_CONFIG)
            if not is_valid:
                logging.error("Configuration validation failed with updates: %s", self.updates)
                GLOBAL_CONFIG.clear()
                GLOBAL_CONFIG.update(self.original_config)
                raise ValueError("Validation failed for the configuration.")

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the context: Restore the original configuration and handle exceptions.
        """
        # Restore the original configuration
        GLOBAL_CONFIG.clear()
        GLOBAL_CONFIG.update(self.original_config)
        logging.info("Restored the original configuration: %s", self.original_config)

        # If an exception occurred, log it
        if exc_type:
            logging.error("Exception occurred: %s", exc_value)


# Example validator function (Optional)
def validate_config(config: dict) -> bool:
    """
    Example validator function to check the validity of the configuration.
    Returns True if the configuration is valid, False otherwise.
    """
    if not isinstance(config.get("feature_a"), bool):
        return False
    if not isinstance(config.get("feature_b"), bool):
        return False
    if not isinstance(config.get("max_retries"), int) or config["max_retries"] < 0:
        return False
    return True


# Example usage
if __name__ == "__main__":
    logging.info("Initial GLOBAL_CONFIG: %s", GLOBAL_CONFIG)

    # Example 1: Successful configuration update
    try:
        with Configuration({"feature_a": False, "max_retries": 5}):
            logging.info("Inside context: %s", GLOBAL_CONFIG)
    except Exception as e:
        logging.error("Error: %s", e)

    logging.info("After context: %s", GLOBAL_CONFIG)

    # Example 2: Configuration update with validation failure
    try:
        with Configuration({"feature_a": "invalid_value", "max_retries": -1}, validator=validate_config):
            logging.info("This should not be printed if validation fails.")
    except Exception as e:
        logging.error("Caught exception: %s", e)

    logging.info("After failed context: %s", GLOBAL_CONFIG)
