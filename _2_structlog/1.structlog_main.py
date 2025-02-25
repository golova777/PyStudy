import logging
import structlog

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.WARNING)
)

logger = structlog.get_logger()


logger.debug("Database connection established")
logger.info("Processing data from the API")
logger.warning("Resource usage is nearing capacity")
logger.error("Failed to save the file. Please check permissions")
logger.critical("System has encountered a critical failure. Shutting down")