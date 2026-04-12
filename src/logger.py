import logging
import os
from datetime import datetime

# Log file ka naam current timestamp ke saath
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Make logs folder if not there and if there just append it.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)