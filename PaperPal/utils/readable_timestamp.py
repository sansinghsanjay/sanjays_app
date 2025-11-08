# python imports
from datetime import datetime, timezone

# get readable timestamp of "now"
def get_readable_timestamp():
    timestamp = datetime.now(timezone.utc).strftime('%d-%m-%Y %H:%M:%S UTC')
    return timestamp