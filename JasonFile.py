import json
from loadJson import LoadJson
class JsonFile:
    def writeData():
        with open("C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\outputvs.txt", "rb") as inputfile:
            data = json.load(inputfile)
        with open("C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\test2vs.json", "w") as outputfile:
            json.dump(data, outputfile, indent=4)
            
        sorted_file = dict(data) #sorting the data according to user_id
        sorted_file['customer'] = sorted(data['customer'], key=lambda x : x['user_id'], reverse=False)


        with open("C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\test2vs.json", "w") as outputfile2:
            json.dump(sorted_file, outputfile2, indent=4)
            print("data sorted")
        LoadJson.LoadData()
