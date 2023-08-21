import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import config


def personal_message_handler(event):
    pass


def chat_message_handler(event):
    pass


if __name__ == "__main__":
    token = config.token
    group_id = config.group_id

    vk_session = vk_api.VkApi(token=token)
    receiver = vk_api.bot_longpoll.VkBotLongPoll(vk_session, group_id)
    vk = vk_session.get_api()

    for event in receiver.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                personal_message_handler(event)
            else:
                chat_message_handler(event)
