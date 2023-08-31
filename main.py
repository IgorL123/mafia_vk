import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import config
import asyncio

{
    "true_chat_id": {
        "current_state": {
            # то что мы храним локально
            "killedUserId": "",
            "healedUserId": "",
            "checkedUserId": ""
        },
        "last_state": {
            # global data
            "users": [
                # инфа по пользователю
            ]
        }
    }
}

session_data = dict()

def get_tci(tui: str) -> str:
    pass

# TODO: дописать
def send_commissar_info_message():
    keyboard_com = VkKeyboard(one_time=True, inline=True)
    for i, "здесь будет массив имен живых игроков" in "сам список живых игроков":
        keyboard_com.add_button("игрок такой-то")
    vk_api.messages.send(message_text="", receiver_user_id="", random_id="", keyboard_com="")

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
