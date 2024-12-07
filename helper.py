import json
import logging

# Configure logging for helper functions
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class Helper:
    @staticmethod
    def read_file(file_name):
        try:
            with open('storage/' + file_name) as f:
                data = json.load(f)
                logger.info(f"Successfully read file: storage/{file_name}")
                return data
        except FileNotFoundError:
            logger.error(f"File not found: storage/{file_name}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON in file: storage/{file_name}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred while reading file: {file_name}, Error: {e}")
            raise

    @staticmethod
    def dump_file(file_name, data):
        try:
            with open('storage/' + file_name, 'w') as f:
                json.dump(data, f, indent=4)
                logger.info(f"Successfully wrote data to file: storage/{file_name}")
        except Exception as e:
            logger.error(f"An unexpected error occurred while writing to file: {file_name}, Error: {e}")
            raise
