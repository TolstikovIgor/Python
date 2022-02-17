def user_info(**kwargs) -> object:
    return ' , '.join(kwargs.values())

print(user_info(
    имя=input('Имя: '),
    фамилия=input('Фамилия: '),
    год_рождения=input('Год рождения: '),
    город_проживания=input('Город проживания: '),
    почта=input('Почта: '),
    телефон=input("Телефон: ")
))
