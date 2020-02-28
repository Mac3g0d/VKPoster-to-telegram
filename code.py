# Bot poster v 1.002 created by Mace @Themaceg0d,call me XD

import telebot
import vk_api
from telebot.types import InputMediaPhoto
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token ='TOKEN'
domain='DOMAIN_ID'
access_token='ACCESS_TOKEN'
chanelid = '@CHANELID'
bot = telebot.TeleBot( token )
vk_session = vk_api.VkApi( token=access_token )
longpoll = VkBotLongPoll( vk_session, domain )

if __name__ == '__main__':
    bot.poling(nonestop=True)
    while True: 
        for event in longpoll.listen():
            if event.type == VkBotEventType.WALL_POST_NEW and event.obj.post_type == 'post':  # Если вышел пост на стене группы, запускает цикл
                if event.object.attachments:
                    img_urls = []
                    for photo in event.object.attachments:
                        if len( img_urls ) != 0:
                            img_urls.append(
                                InputMediaPhoto( media=photo['photo']['photo_604'] ) )  # Собираем все картинки из поста
                        else:
                            img_urls.append(
                                InputMediaPhoto( media=photo['photo']['photo_604'], caption=str( event.obj.text ) ) )

                    if len( img_urls ) != 0:
                        bot.send_media_group( chanelid, img_urls ) # Отправляем альбом с фотками и caption

                else:
                    bot.send_message( chanelid, str( event.obj.text ) ) 
