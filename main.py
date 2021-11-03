# Dependencias
# controlador de mensajes, maneja mensajes de textos de cualquier chat, se trabaja con add_handler (handle= manipular)
from pyrogram.handlers import MessageHandler
from pyrogram import Client as ClientTg
from environs import Env
from pyrogram.types import Message
from pyrogram.types import Chat
from Filtro import Filtro


# from Readers.filtro import CHANNEL_CODES

env = Env()  # carga la informacion en env
env.read_env()

NAME_SESSION = env("NAME_SESSION")
API_ID = env("API_ID_TELEGRAM")
API_HASH = env("API_HASH_TELEGRAM")
RECIPIENT_CHANNEL_CODE = env("RECIPIENT_CHANNEL_CODE_TELEGRAM_TEST")

filtro=Filtro()

async def enviador(client:ClientTg, message:Message):

    await client.forward_messages(RECIPIENT_CHANNEL_CODE,message.chat.id,message.pinned_message.message_id)

def main():
    app_tg = ClientTg(NAME_SESSION, API_ID, API_HASH)
    app_tg.add_handler(MessageHandler(enviador, filtro.channel_filter()))

    app_tg.run()


if __name__ == '__main__':
    main()