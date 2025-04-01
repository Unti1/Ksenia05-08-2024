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

class RatingEnum(str, Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10



