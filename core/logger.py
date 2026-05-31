# logger.py

import logging
import os
from logging.handlers import RotatingFileHandler


# =========================
# Create logs directory
# =========================
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")


# =========================
# Logger Formatter
# =========================
LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

formatter = logging.Formatter(LOG_FORMAT)


# =========================
# Main Logger Function
# =========================
def get_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # =========================
    # Console Handler
    # =========================
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # =========================
    # File Handler
    # =========================
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3,
    )

    file_handler.setFormatter(formatter)

    # =========================
    # Add Handlers
    # =========================
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger
logger=get_logger("app.log")