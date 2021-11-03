from environs import Env, Subcast 
#libreria pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

env=Env()
env.read_env()
CHANNEL_CODES_READED=env.list('CHANNEL_CODES_READED', subcast=int)
CHANNEL_NAMES_READED=env.list("CHANNEL_NAMES_READED")
RECIPIENT_CHANNEL_CODE = env("RECIPIENT_CHANNEL_CODE_TELEGRAM_TEST")

class Filtro:
    _message:None

    def channel_filter(self):
        """ Aplica y crea el filtro """
        return filters.create(self.nft_filter)

    async def nft_filter(self,client:Client,message:Message):
        """
        Filtra el contenido de los canales cuando son pinneados
            Parametros:
                client: object type Client Pyrogram client info
                message: object type Message mensaje capturado
        """
        self.client=client
        self._message=message
        #funcion devuelve un booleano si el filtro se cumple o no.
        
        if self._message.chat.id in CHANNEL_CODES_READED and self._message.pinned_message:
            #print(f"message.chat.title: {self._message.chat.title}")
            #print(f"message.chat.id: {self._message.chat.id}")
            #print(f"message.message_id: {self._message.message_id}")
            #print(f"message.pinned_message.message_id: {self._message.pinned_message.message_id}")
            return True
        else:
            return False