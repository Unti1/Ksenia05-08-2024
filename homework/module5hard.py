'''2023/11/05 00:00|Дополнительное практическое задание по модулю*
Дополнительное практическое задание по модулю: "Классы и объекты."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же учитывайте следующие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"

Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')'''
import hashlib
import time
class User:
    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        self.age = age
 

class Video:
    def __init__(self,title,duration,time_now = 0,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users:list[User] = []
        self.videos = []
        self.current_user = None
    


    def login(self,nickname, password):
        for user in self.users:
            if nickname == user.nickname:
                if int(hashlib.sha256(password.encode()).hexdigest(), 16) == user.password:
                    self.current_user = user 
                    print(f'{user} создан!')

    def log_out(self):
        self.current_user = None

    def register(self,nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.')
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        return f"Пользователь {nickname} успешно зарегистрирован и вошёл в систему"
                
    def add(self,other:Video):
        for x in self.videos:
            if other.title == x.title: # показать по строкам как работает 
                return 'No'
                
        self.videos.append(other)
        return "Готово"
    
    def get_videos(self,name):
        result =[]
        for x in self.videos:
            if name.lower() in x.title.lower():
                result.append(x.title) 
        return result
    
    def watch_video(self,name):
        if not self.current_user:
            return "Войдите в аккаунт, чтобы смотреть видео."
            

        for x in self.videos:
            if name.lower() == x.title.lower():
            # Проверяем ограничение 18+
                if x.adult_mode and self.current_user.age < 18:
                    return "Вам нет 18 лет, пожалуйста покиньте страницу."
                    
                print(f"Начинаем просмотр видео '{x.title}'.")
                for second in range(x.time_now, x.duration):
                    print(f"Секунда {second + 1}")
                    time.sleep(1)  # Пауза между выводами
                x.time_now = 0
                return "Конец видео."
        return "Видео не найдено."
                
            
    
                    
                

            


                
        
        
        

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 20243 года', 200)

# Добавление видео
print(ur.add(v1))
print(ur.add(v2))
print(ur.add(v2))
print(ur.add(v3))
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.watch_video('Для чего девушкам парень программист?'))
print(ur.register('vasya_pupkin', 'lolkekcheburek', 13))
print(ur.register('vasya_pupkin', 'lolkekcheburek', 13))
print(ur.watch_video('Для чего девушкам парень программист?'))
print(ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25))
print(ur.watch_video('Для чего девушкам парень программист?'))








    
            
        
