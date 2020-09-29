import vk_api
import json

group_id = -185975489

def auth_handler():
    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: true - сохранить, false - не сохранять.
    remember_device = True
    return key, remember_device

def stop_f(items):
    print (items)

def main():
    login, password = '', ''
    vk_session = vk_api.VkApi(
    login, password,
    auth_handler=auth_handler) # функция для обработки двухфакторной аутентификации

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
    tools = vk_api.VkTools(vk_session)
    wall = tools.get_all('wall.get', 100,
                         {'owner_id': group_id})
    print('Posts count:', wall['count'])
    f = open(r" wall_asp.txt", 'a')
    f.write(json.dumps(wall))
    f.close()

if __name__ == '__main__':
    main()

