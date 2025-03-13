from enum import Enum

class GenderEnum(str, Enum):
    MALE = 'Мужчина'
    FEMALE = 'Женщина'

class ProfessionEnum(str, Enum):
    ADMIN = 'Администратор'
    ENGINEER = 'Инженер'
    DOCTOR = 'Доктор'
    TECHNOLOGIST = 'Технологист'
    MANAGER = 'Менеджер'
    TECHNOLOGY_LEAD = 'Технологийный лидер'
    PROJECT_MANAGER = 'Проектный менеджер'
    PROJECT_LEADER = 'Проектный лидер'
    UNEMPLOYED = 'Не работающий'

class StatusEnum(str, Enum):
    PUBLISHED = 'опубликован'
    DELETED = 'удален'
    UNDER_MODERATION = 'в модерации'
    DRAFT = 'черновик'
    SCHEDULED = 'отложенная публикация'

