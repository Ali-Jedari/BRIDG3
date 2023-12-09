'''
Telegram Message Processor
'''

from numpy import nan

def process_text(msg):
    '''
    Process message texts
    '''
    message = msg.strip('\\')
    lines = message.split('\n')
    print(lines)
    what, when, where, why = nan, nan, nan, nan

    for line in lines:
        l = line.upper()
        if ("WHAT:" in l or "WHAT?" in l) and what is nan:
            what = l.replace("WHAT", "")[1:].strip()

        if ("WHEN:" in l or "WHEN?" in l) and when is nan:
            when = l.replace("WHEN", "")[1:].strip()

        if ("WHERE:" in l or "WHERE?" in l) and where is nan:
            where = l.replace("WHERE", "")[1:].strip()

        if ("WHY:" in l or "WHY?" in l) and why is nan:
            why = l.replace("WHY", "")[1:].strip()

    print(f'what: {what}, when: {when}, where: ')
    return {'What': [what], 'When': [when], 'Where': [where], 'Why': [why]}
