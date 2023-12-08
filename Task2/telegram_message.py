'''
Access Telegram Channels and Get New Messages
'''

from telethon import TelegramClient, events

API_ID = '25857802'
API_HASH = '186d136e6730a05a749a09e5a9bbda63'
client = TelegramClient('anon', API_ID, API_HASH)

channels = ['bridg3_test', 'skilta', 'infoluuppi', 'intoreminder', 'tiedotus',
       'TARAKItiedottaa', 'ykinkuumalinja', 'tietoteekkarikilta',
       'tampereenteekkarit', 'indecs', 'miktiedotus', 'ttkamerattiedotus',
       'treytiedottaa', 'hiukkanentiedotus', 'tekopiskelijat']

indicators = ['party', 'Party', 'PARTY', 'Event', 'event', 'EVENT']

@client.on(events.NewMessage(chats=channels))
async def process_telegram_msg(event):
    '''
    Processes new messages from Telegram channels
    And stores in a csv file
    '''
    msg = event.raw_text
    await client.send_message(entity='what_where_when_event_notifier', message='Moikka!')
    if any(ind in msg for ind in indicators):
        # TODO: process the msg
        pass

client.start()
client.run_until_disconnected()
