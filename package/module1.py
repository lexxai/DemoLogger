import logging

logger: logging = logging.getLogger(__name__)


def some_code1():
    logger.info("INFO M1")
    logger.debug("DEBUG M1")
    logger.error("ERROR M1")
