import datetime
import logging
from pytz import timezone

class MoscowTimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        record_time = datetime.datetime.fromtimestamp(record.created, tz=timezone('Europe/Moscow'))
        if datefmt:
            return record_time.strftime(datefmt)
        return record_time.isoformat()

logging.root.setLevel(logging.INFO)

file_handler = logging.FileHandler('logs.log')
# Использование времени без учета конкретной временной зоны.
# file_handler.setFormatter(logging.Formatter("%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s"))
# Если нужно использовать конкретную временной зону, можно использовать наш MoscowTimeFormatter.
file_handler.setFormatter(MoscowTimeFormatter("%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s", datefmt='%d.%m %H:%M:%S'))
logging.root.addHandler(file_handler)