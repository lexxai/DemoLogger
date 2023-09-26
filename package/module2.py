import logging

logger: logging = logging.getLogger(__name__)


def some_code2():
    logger.info("INFO M2")
    logger.debug("DEBUG M2")
    logger.error("ERROR M2")
