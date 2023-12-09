from numpy import nan

def process_text(msg):
    '''
    Process message texts
    '''
    lines = msg.split('\n')
    what, when, where, why = nan, nan, nan, nan

    for line in lines:
        l = line.upper()
        if "WHAT" in l and what is nan:
            what = l.replace("WHAT", "")[1:]

        if "WHEN" in l and when is nan:
            when = l.replace("WHEN", "")

        if "WHERE" in l and where is nan:
            where = l.replace("WHERE", "")

        if "WHY" in l and why is nan:
            why = l.replace("WHY", "")

    print(f'what: {what}, when: {when}, where: ')
    return {'What': [what], 'When': [when], 'Where': [where], 'Why': [why]}
