# Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России.

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def task_1():
    geo_logs_rus =[]
    for geo_logs_dict in geo_logs:
        for key, value in geo_logs_dict.items():
            if 'Россия' in value[1]:
                geo_logs_rus.append(geo_logs_dict)
    return geo_logs_rus

# Выведите на экран все уникальные гео-ID из значений словаря ids.

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def task_2():
    geo = set()
    for i in ids.values():
        geo.update(i)
    return list(geo)



# Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
dict_queries = {}
count = 0


def task_3():

    for i in queries:
        j = len(i.split())
        dict_queries[j] = dict_queries.get(j, 0) + 1
    return f'Поисковых запросов из двух слов составляет:{int(dict_queries[2]/len(queries)*100)} %',\
        f'Поисковых запросов из трёх слов составляет:{int(dict_queries[3]/len(queries)*100)} %'


def task_4():
    stats = {'facebook': 5, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    return max(stats, key = stats.get)

