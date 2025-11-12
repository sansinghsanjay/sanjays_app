# python imports
import logging
import sys
import traceback

# utils imports
from utils.readable_timestamp import get_readable_timestamp

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler("app.log", mode="a"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)
logger.info(f'[INFO] app.py: starting the app\n')

# log messages
def log_status(status: str, source: str, timestamp: str, msg: str):
    try:
        # check the status and log accordingly
        if(status == "INFO" or status == "WARNING"):
            logger.info(f'[{status}] {source} ({timestamp}): {msg}\n')
        else:
            logger.error(f'[{status}] {source} ({timestamp}): {msg}\n')
    except Exception as e:
        timestamp = get_readable_timestamp()
        logger.error(f'[ERROR] /utils/logger.py ({timestamp}): {e}')
        traceback.print_exc()