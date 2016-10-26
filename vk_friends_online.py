import vk

APP_ID = 5578596


def get_user_login():
    return input('"Кто онлайн ВК"\nВведите логин:\n')


def get_user_password():
    return input('\nВведите пароль:\n')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    return api.friends.get(fields={'online'})


def output_friends_to_console(friends_online):
    friends_online_list = [' '.join([friend['first_name'], friend['last_name']])
                           for friend in friends_online if friend['online']]
    friends_online_number = len(friends_online_list)
    print('\nТвои друзья в онлайне\nСколько: {}\nКто:'.format(friends_online_number))
    for friend in friends_online_list:
        print(friend)

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
