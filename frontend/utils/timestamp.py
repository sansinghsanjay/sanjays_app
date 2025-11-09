# python imports
from datetime import datetime, timezone

# return current timestamp in readable form
def get_current_timestamp():
    timestamp = datetime.now(timezone.utc).strftime("%d-%m-%Y %H:%M:%S UTC")
    return timestamp