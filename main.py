from mapbook_lib.model import  users
from mapbook_lib.controller import  read_data, add_user


def add_user(users_data: list)->None:


    name=input('Podaj imię: ')
    location=input('Podaj lokalizację: ')
    posts=int(input('Podaj liczbę postów'))
    usermessage=[]
    users_data.append( {'username': name, 'location': location, 'posts': posts,
         'usermessage': usermessage} ,)




while True:
    print('0 - zakoncz program')
    print('1 - wyswietl znajomych')
    print('2 - dodaj znajomego')

    choose=input('wybierz opcje: ')
    if choose == '0':
        break
    if choose == '1':
        read_data(users[1:])
    if choose == '2':
        add_user(users)