import json
from distance import CalculateDistance
class LoadJson:
    def LoadData():
        with open("C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\test2vs.json", "r") as read_file:
            data = json.load(read_file)

        CalculateDistance.distance(data)
