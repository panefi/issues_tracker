import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file = "logs/fastapi_app.log"

    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)  # 5MB per file, 5 backups
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.DEBUG)

    logging.basicConfig(handlers=[file_handler, console_handler], level=logging.DEBUG)
    # logging.getLogger().info("Logging setup complete")
