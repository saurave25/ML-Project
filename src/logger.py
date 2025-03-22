#Python logging is a way to track events in your code, like errors or important actions, 
# for debugging and monitoring purposes.
#The logging module in Python is a ready-to-use and 
# powerful module that is designed to meet the needs of beginners as well as enterprise teams.

import logging
import os
from datetime import datetime

# Define log directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)  # Create logs directory if it doesn't exist
#🔹 Why is this needed?
# To keep log files organized in a separate folder instead of cluttering the main directory.

# Define log file name
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)  # Correct path to log file

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example log message
if __name__ == "__main__":
    logging.info("Logging has started")
