import vk
import getpass
APP_ID = 5578596


def get_user_login():
    return input('"Кто онлайн ВК"\nВведите логин:\n')


def get_user_password():
    return getpass.getpass('\nВведите пароль:\n')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id = APP_ID,
        user_login = login,
        user_password = password,
        scope = ('friends')
    )
    api = vk.API(session)
    online_user_ids = set(api.friends.getOnline())
    return api.users.get(user_ids = online_user_ids)


def output_friends_to_console(friends_online_list):
    print('Твои друзья в онлайне\nСколько: {}\nКто:'.format(len(friends_online_list)))
    for friend in friends_online_list:
        print(' '.join([friend['first_name'], friend['last_name']]))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
