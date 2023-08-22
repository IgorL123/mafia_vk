import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import config
import asyncio


async def personal_message_handler(event):
    pass

async def game_master(event):
    ...

async def chat_message_handler(event):

    '''

    This function works with everything that`s is connected with public chats:
        initializing games
        starting games
        aborting  games
        sending information to server when game was started
        providing helpful information for users including game rules
        maybe ( will be added )

    :param event:
    :return:
    '''

    try:
        random_id = get_random_id()
        received_message = event.object.message['text']
        match received_message[:received_message.index(' ')]: # TODO make get using api receiving day time information
            case '/help':
                ...
            case '/init_mafia':
                ...
            case '/start_mafia':
                ...
            case '/bot':    # create buttons
                ...
    except KeyError:
        # receive chat id and print to chat rules
        ...

async def main():
    token = config.token
    group_id = config.group_id

    vk_session = vk_api.VkApi(token=token)
    receiver = vk_api.bot_longpoll.VkBotLongPoll(vk_session, group_id) # TODO : write greetings

    for event in receiver.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                await personal_message_handler(event)
            else:
                await chat_message_handler(event)

if __name__ == "__main__":
    asyncio.run(main())

# TODO : do not forget to add the third winnig way
# TODO : write greetings when adding to a new chat
# TODO : when was added to a new chat start listening it and when a new message /init_mafia is writtent
#        write to all players randomly generated local id ( check that

"""
<vk_api.bot_longpoll.VkBotLongPoll object at 0x000001C557F17400>
<<class 'vk_api.bot_longpoll.VkBotMessageEvent'>({'group_id': 222124211, 'type': 'message_new', 'event_id': '8d52b027845f0e551154fb04576da6e3efeafd4c', 'v': '5.131', 'object': {'message': {'date': 1692707952, 'from_id': 260931038, 'id': 0, 'out': 0, 'attachments': [], 'conversation_message_id': 14, 'fwd_messages': [], 'important': False, 'is_hidden': False, 'peer_id': 2000000001, 'random_id': 0, 'text': 'a'}, 'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback', 'intent_subscribe', 'intent_unsubscribe'], 'keyboard': True, 'inline_keyboard': True, 'carousel': True, 'lang_id': 0}}})> <class 'vk_api.bot_longpoll.VkBotMessageEvent'>
<<class 'vk_api.bot_longpoll.VkBotEvent'>({'group_id': 222124211, 'type': 'message_typing_state', 'event_id': 'd82dd58b8c4ee71baf24f3a88f1bd14968db5c1e', 'v': '5.131', 'object': {'state': 'typing', 'from_id': 260931038, 'to_id': -222124211}})> <class 'vk_api.bot_longpoll.VkBotEvent'>
<<class 'vk_api.bot_longpoll.VkBotMessageEvent'>({'group_id': 222124211, 'type': 'message_new', 'event_id': '3ab8212dc2ace626a4ba98a084cd1fa2bcd9b7db', 'v': '5.131', 'object': {'message': {'date': 1692707958, 'from_id': 260931038, 'id': 20, 'out': 0, 'attachments': [], 'conversation_message_id': 14, 'fwd_messages': [], 'important': False, 'is_hidden': False, 'peer_id': 260931038, 'random_id': 0, 'text': 'f'}, 'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback', 'intent_subscribe', 'intent_unsubscribe'], 'keyboard': True, 'inline_keyboard': True, 'carousel': True, 'lang_id': 0}}})> <class 'vk_api.bot_longpoll.VkBotMessageEvent'>
<<class 'vk_api.bot_longpoll.VkBotMessageEvent'>({'group_id': 222124211, 'type': 'message_new', 'event_id': '63f241f6a99dd0982312bbd9744a7c4bc3224ba4', 'v': '5.131', 'object': {'message': {'date': 1692707996, 'from_id': 260931038, 'id': 0, 'out': 0, 'action': {'type': 'chat_invite_user', 'member_id': -222124211}, 'attachments': [], 'conversation_message_id': 2, 'fwd_messages': [], 'important': False, 'is_hidden': False, 'peer_id': 2000000002, 'random_id': 0, 'text': ''}, 'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback', 'intent_subscribe', 'intent_unsubscribe'], 'keyboard': True, 'inline_keyboard': True, 'carousel': True, 'lang_id': 0}}})> <class 'vk_api.bot_longpoll.VkBotMessageEvent'>
<<class 'vk_api.bot_longpoll.VkBotMessageEvent'>({'group_id': 222124211, 'type': 'message_new', 'event_id': '944db9eb58837e5168281c32774afb3b788f16f2', 'v': '5.131', 'object': {'message': {'date': 1692708041, 'from_id': 260931038, 'id': 0, 'out': 0, 'attachments': [], 'conversation_message_id': 4, 'fwd_messages': [], 'important': False, 'is_hidden': False, 'peer_id': 2000000002, 'random_id': 0, 'text': '[club222124211|@public222124211]'}, 'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback', 'intent_subscribe', 'intent_unsubscribe'], 'keyboard': True, 'inline_keyboard': True, 'carousel': True, 'lang_id': 0}}})> <class 'vk_api.bot_longpoll.VkBotMessageEvent'>"""