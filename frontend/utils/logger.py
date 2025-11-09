# python imports
import logging
import sys
import traceback

# utils imports
from utils.timestamp import get_current_timestamp

# configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler("app.log", mode="a"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)
logger.info(f"[INFO] /utils/logger.py ({get_current_timestamp()}): Logger created\n")

# log messages
def log_status(status: str, source: str, timestamp: str, msg: str):
    try:
        if(status == "INFO" or status == "WARNING"):
            logger.info(f"[{status}] {source} ({timestamp}): {msg}\n")
        elif(status == "ERROR"):
            logger.error(f"[{status}] {source} ({timestamp}): {msg}\n")
        else:
            logger.error(f"[ERROR] {source} ({timestamp}): Invalid status for a log message: {status}\n")
    except Exception as e:
        logger.error(f"[ERROR] /utils/logger.py ({get_current_timestamp()}): {e}; traceback: {traceback.print_exc()}\n")