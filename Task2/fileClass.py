class File:
    def __init__(self, fileIn, fileOut):
        self.__fileRead = fileIn
        self.__fileWrite = fileOut

        self.__output_data = {}

    def process_file(self):
        for lines in self.__fileRead:
            lines = lines.strip()
            if "What" in lines:
                self.__output_data.update({"Event": lines.replace("What:", "")})

            if "When" in lines:
                self.__output_data.update({"Date": lines.replace("When:", "")})

            if "Where" in lines:
                self.__output_data.update({"Location": lines.replace("Where:", "")})

            if "Why" in lines:
                self.__output_data.update({"Why": lines.replace("Why:", "")})

        if len(self.__output_data) > 0:
            for question, text in self.__output_data.items():
               print(question,":",text,  file = self.__fileWrite)