import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import config


async def personal_message_handler(event):
    pass


async def chat_message_handler(event):
    pass


if __name__ == "__main__":
    token = config.token
    vk = vk_api.VkApi(token=token)
    receiver = VkLongPoll(vk)

    for event in receiver.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                personal_message_handler(event)
            else:
                chat_message_handler(event)
