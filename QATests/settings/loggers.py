import datetime
import logging
from pytz import timezone

class MoscowTimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        record_time = datetime.datetime.fromtimestamp(record.created, tz=timezone('Europe/Moscow'))
        if datefmt:
            return record_time.strftime(datefmt)
        return record_time.isoformat()

# logging.root.setLevel(logging.INFO)

# file_handler = logging.FileHandler('logs.log')
# # Использование времени без учета конкретной временной зоны.
# # file_handler.setFormatter(logging.Formatter("%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s"))
# # Если нужно использовать конкретную временной зону, можно использовать наш MoscowTimeFormatter.
# file_handler.setFormatter(MoscowTimeFormatter("%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s", datefmt='%d.%m %H:%M:%S'))
# logging.root.addHandler(file_handler)

# Обработчик для какого то конкретного 

database_logger = logging.getLogger("database") # Создаем логгер для базы данных "database" просто название
database_logger.setLevel(logging.ERROR)
database_file_logger = logging.FileHandler('logs/database.log', encoding='utf-8') # Создаем файловый обработчик для базы данных "database"
database_file_logger.setFormatter(logging.Formatter("%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s"))
database_logger.addHandler(database_file_logger) # Добавляем файловый обработчик для базы данных "database" в логгер "database"
# С этого момента, мы можем обращаться не к logging а к конкретному объекту


# Добавим ещё один обработчик
database_2_logger = logging.getLogger("database2") # Создаем логгер для базы данных "database" просто название
database_2_logger.setLevel(logging.WARNING)
database_2_file_logger = logging.FileHandler('logs/database.log', encoding='utf-8') # Подключаемся к тому же файлу что и первая база данных
database_2_file_logger.setFormatter(
    MoscowTimeFormatter(
            fmt="%(asctime)s |  %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
            datefmt='%m.%d %H:%M:%S'
        )
    )
database_2_logger.addHandler(database_file_logger) # Добавляем файловый обработчик для базы данных "database" в логгер "database"
# С этого момента, мы можем обращаться не к logging а к конкретному объекту
