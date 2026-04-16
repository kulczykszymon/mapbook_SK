

users: list = [
    {'username': 'oliwia' , 'location':'łódź','posts':1,'usermessage':['{życzenia1', 'kochamlegie' , 'sprzedam opla', 'kiwi1']},
    {'username': 'paweł' , 'location':'ostroda','posts':2,'usermessage':['życzenia2', 'kochamlegie' , 'sprzedam opla', 'kiwi1']},
    {'username': 'eliza' , 'location':'radom','posts':3,'usermessage':['życzenia3', 'kochamlegie' , 'sprzedam opla', 'kiwi1']},
    {'username': 'filip' , 'location':'dęblin','posts':4,'usermessage':['życzenia4', 'kochamlegie' , 'sprzedam opla', 'kiwi1']},
]

for user in users[1:]:
    print(f'twój znajomy {user['username']} z miejscowości [{user["location"]} opublikował {user["posts"]} wiadomości o treści. Ostatnia wiadomość {user['usermessages']}')
    
#     twoj znajomy filip z miejscowości Dęblin opublikował 1 post o treści: życzenia
