'''
Access Telegram Channels and Get New Messages
'''

from os import listdir
from telethon import TelegramClient, events
from process_text import process_text
import pandas as pd
from numpy import nan

API_ID = '25857802'
API_HASH = '186d136e6730a05a749a09e5a9bbda63'
client = TelegramClient('anon', API_ID, API_HASH)

channels = ['bridg3_test', 'skilta', 'infoluuppi', 'intoreminder', 'tiedotus',
       'TARAKItiedottaa', 'ykinkuumalinja', 'tietoteekkarikilta',
       'tampereenteekkarit', 'indecs', 'miktiedotus', 'ttkamerattiedotus',
       'treytiedottaa', 'hiukkanentiedotus', 'tekopiskelijat']

ENTITY = 'Wright_Channel'
FNAME = 'Events.csv'

@client.on(events.NewMessage(chats=channels))
async def process_telegram_msg(event):
    '''
    Processes new messages from Telegram channels
    And stores in a csv file
    '''
    message = event.raw_text

    #if any(indicator in message for indicator in indicators):
    message_dict = process_text(message)
    if FNAME in listdir():
        events_dataframe = pd.read_csv(FNAME, index_col=0)
        events_dataframe = pd.concat([events_dataframe, pd.DataFrame(message_dict)], axis=0)
        events_dataframe.to_csv(FNAME)
    else:
        events_dataframe = pd.DataFrame(message_dict)
        events_dataframe.to_csv(FNAME)

    new_msg = f'New event!\nhttps://t.me/{event.sender.username}/{event.id}\n\n'
    for item in message_dict.items():
        if item[1][0] is not nan:
            new_msg = new_msg + item[0] + ": " + str(item[1][0]) + '\n'

    await client.send_message(entity=ENTITY, message=new_msg)

client.start()
client.run_until_disconnected()
