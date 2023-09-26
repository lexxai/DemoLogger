import logging
from pathlib import Path

logged_format = "%(asctime)s [%(levelname)s] #%(process)s (%(name)s) %(message)s"
logged_format_date = "%Y-%m-%d %H:%M:%S"
logged_formatter = logging.Formatter(logged_format, datefmt=logged_format_date)


def get_logger(name: str, log_path: Path | None = None) -> logging:
    log_path: Path = Path() if log_path is None else log_path
    log_path.mkdir(exist_ok=True, parents=True)

    # create file handler for DEBUG, INFO
    file_name = "debug.log"
    file_path = log_path.joinpath(file_name)
    logged_handler_file = logging.FileHandler(str(file_path))
    logged_handler_file.setLevel(logging.DEBUG)
    logged_handler_file.setFormatter(logged_formatter)

    # create file handler for ERRORS
    file_name = "error.log"
    file_path = log_path.joinpath(file_name)
    logged_handler_error_file = logging.FileHandler(str(file_path))
    logged_handler_error_file.setLevel(logging.ERROR)
    logged_handler_error_file.setFormatter(logged_formatter)

    # create console handler INFO, ERROR
    logged_handler_stream = logging.StreamHandler()
    logged_handler_stream.setLevel(logging.INFO)
    logged_handler_stream.setFormatter(logged_formatter)

    # create main logger for all child modules of thi package
    print(f"{name=}")
    my_logger: logging = logging.getLogger(name)
    my_logger.addHandler(logged_handler_file)
    my_logger.addHandler(logged_handler_error_file)
    my_logger.addHandler(logged_handler_stream)
    my_logger.setLevel(logging.DEBUG)
    return my_logger
