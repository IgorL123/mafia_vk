import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import config
import asyncio


async def personal_message_handler(event):
    pass


async def chat_message_handler(event):
    pass


async def main():
    token = config.token
    group_id = config.group_id

    vk_session = vk_api.VkApi(token=token)
    receiver = vk_api.bot_longpoll.VkBotLongPoll(vk_session, group_id)

    for event in receiver.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                await personal_message_handler(event)
            else:
                await chat_message_handler(event)

if __name__ == "__main__":
    asyncio.run(main())
