
def create_logger(log_level):

    def log(message, level):
        if level >= log_level:
            print(f'[{level}] {message}')
    
    def set_log_level(new_level):
        nonlocal log_level
        log_level = new_level
    
    def get_log_level():
        return log_level
    # print(locals())
    return log, set_log_level, get_log_level
# print(globals())

if __name__ == '__main__':
    log, set_log_level, get_log_level = create_logger(2)
    log("Это информационное сообщение", 1)
    log("Предупреждение", 2)
    log("Ошибка", 3)

    print(f"Текущий уровень логирования: {get_log_level()}")
    set_log_level(1)
    print(f"Новый уровень логирования: {get_log_level()}")
    log("Тепель этот вывод", 1)
    log("Предупреждение", 2)
    log("Ошибка", 3)
