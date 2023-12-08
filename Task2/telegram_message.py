'''
Access Telegram Channels and Get New Messages
'''

from os import listdir
from telethon import TelegramClient, events
from process_text import process_text
import pandas as pd

API_ID = '25857802'
API_HASH = '186d136e6730a05a749a09e5a9bbda63'
client = TelegramClient('anon', API_ID, API_HASH)

channels = ['bridg3_test', 'skilta', 'infoluuppi', 'intoreminder', 'tiedotus',
       'TARAKItiedottaa', 'ykinkuumalinja', 'tietoteekkarikilta',
       'tampereenteekkarit', 'indecs', 'miktiedotus', 'ttkamerattiedotus',
       'treytiedottaa', 'hiukkanentiedotus', 'tekopiskelijat']

indicators = ['party', 'Party', 'PARTY', 'Event', 'event', 'EVENT']
ENTITY = 'what_where_when_event_notifier'
FNAME = 'Events.xlsx'

@client.on(events.NewMessage(chats=channels))
async def process_telegram_msg(event):
    '''
    Processes new messages from Telegram channels
    And stores in a csv file
    '''
    msg = event.raw_text

    if any(ind in msg for ind in indicators):
        d = process_text(msg)
        if FNAME in listdir():
            df = pd.read_excel(FNAME)
            df = pd.concat([df, pd.Series(d)], axis=1)
            df.to_excel(FNAME)
        else:
            df = pd.DataFrame(d)
            df.to_excel(FNAME)

        #new_msg = f'New event posted @{}'
        await client.send_message(entity=ENTITY, message=msg)

client.start()
client.run_until_disconnected()
