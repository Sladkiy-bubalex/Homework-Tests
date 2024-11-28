# Функции из первой задачи

documents = [
            {"type": "passport", "number": "2207 876234", "name": "Иван Иванов"},
            {"type": "inn", "number": "325878234", "name": "Сергей Любимов"},
            {"type": "snils", "number": "7356 7647922", "name": "Иван Иванов"},
            {"type": "passport", "number": "2433 457879", "name": "Сергей Любимов"}
        ]

directories = {'1': ['325878234', '2433 457879'],
               '2': ['7356 7647922', '2207 876234']
}

def get_name(number):
    for document in documents:
        if document["number"] == number:
            return document["name"]
    return "Документ не найден"

def get_directory(number_doc):
    for directory in directories:
        if number_doc in directories[directory]:
            return directory
    return "Полки с таким документом не найдено"

def add(type_, number, name, directoria):
    documents.append({"type": type_, "number": number, "name": name})
    directories[str(directoria)].append(number)
    return documents, directories

# Функции из второй задачи

def discriminant(a, b, c):
    discriminant = b**2-4*a*c
    return discriminant

def solution(a, b, c):
    d = discriminant (a,b,c)
    if d < 0:
        return ('корней нет')
    elif d > 0:
        x_1 = (-b - d**0.5) / (2 * a)
        x_2 = (-b + d**0.5) / (2 * a)
        return (x_2, x_1)
    elif d == 0:
        x = -b / (2 * a)
        return (x)

# Функции из третьей задачи

def vote(votes):
    max_count = {}
    for i in votes:
        max_count[i] = votes.count(i)
    return max(max_count, key=max_count.get)

print(vote([4,7,9,11,4,7,3]))