import logging
from pathlib import Path

from package.logger import get_logger
from package.module1 import some_code1
from package.module2 import some_code2


def init_logger(arg_log_path: Path):
    return get_logger("package", arg_log_path)


logger: logging

if __name__ == "__main__":
    logger = init_logger(Path("logs"))
    logger.info("INFO")
    logger.debug("DEBUG")
    logger.error("ERROR")
    some_code1()
    some_code2()
