
def read_data(users_data: list)-> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowości {user["location"]} opublikował {user["posts"]} wiadomości o treści. Ostatnia wiadomość {user['usermessage'][-1]}')
