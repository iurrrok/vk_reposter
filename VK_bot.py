import vk_api        #pip install vk_api
import time

LOGIN =        #логин от ВК(номер(+ и т д ) или почту)
PASSWORD =        # Пароль от вк
GROUP_ID = -()      # Айди группы берем из линка на группу https://vk.com/public200714338  т е 200714338
TIMER = 60      # Время как часто бот будет проверять наличие новых постов






k=[]

def main():
    """ Пример получения последнего сообщения со стены """

    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    """ VkApi.method позволяет выполнять запросы к API. В этом примере
        используется метод wall.get (https://vk.com/dev/wall.get) с параметром
        count = 1, т.е. мы получаем один последний пост со стены текущего
        пользователя.
    """
    response = vk.wall.get(count=1)  # Используем метод wall.get
    #print(vk.messages.getChat())
    
    #mem = 0

    if response['items']:
        try:
            if response['items'][0]['id'] not in k:
                mes= response['items'][0]['text']
                att1= response['items'][0]['owner_id']
                att2= response['items'][0]['attachments'][0]['photo']['id']
                print(att1,att2)
                print(vk.wall.post(owner_id=GROUP_ID,message=mes,attachments = [ 'photo{}_{}'.format(att1, att2) ]))
                k.append(response['items'][0]['id'])
            else:
                pass

            
            
            
            
            
        except:
            print('nope')


if __name__ == '__main__':
    while True:
        main()
        time.sleep(TIMER)
