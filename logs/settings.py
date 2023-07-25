import logging

# Log levels
LOG_LEVEL = logging.DEBUG  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Log format
LOG_FORMAT = '%(asctime)s [%(levelname)s] [%(name)s]: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Log file path
LOG_FILE = 'logs/app.log'  # The path to the log file, relative to the project root

# Log file size (in bytes)
LOG_FILE_MAX_SIZE = 5242880  # 5 MB

# Log backup count
LOG_FILE_BACKUP_COUNT = 5  # Number of backup log files to keep

# Configure logging
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT, datefmt=DATE_FORMAT, filename=LOG_FILE)
