from numpy import nan

def process_text(msg):
    lines = msg.split('\n')
    what, when, where, why = nan, nan, nan, nan

    for line in lines:
        line = line.strip()
        if "What" in line and what is nan:
            #self.__output_data.update({"Event": lines.replace("What:", "")})
            what = line.strip().replace("What:", "")

        if "When" in line and when is nan:
            #self.__output_data.update({"Date": lines.replace("When:", "")})
            when = line.strip().replace("When:", "")

        if "Where" in line and where is nan:
            #self.__output_data.update({"Location": lines.replace("Where:", "")})
            where = line.strip().replace("Where:", "")

        if "Why" in line and why is nan:
            #self.__output_data.update({"Why": lines.replace("Why:", "")})
            why = line.strip().replace("Why:", "")

    return {'What': [what], 'When': [when], 'Where': [where], 'Why': [why]}

    '''if len(self.__output_data) > 0:
        for question, text in self.__output_data.items():
            print(question,":",text,  file = self.__fileWrite)'''