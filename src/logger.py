import logging
import os
from datetime import datetime

# Create unique log file name so we don't overwrite old logs
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Put all logs in a separate folder to keep project organized
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging to help debug issues when they happen
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Include timestamp and line number for easier debugging
    level=logging.INFO,  # Capture info, warnings, and errors (not just errors)
)