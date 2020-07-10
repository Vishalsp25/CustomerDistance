from math import sin, cos, sqrt, atan2, radians
from deletecontent import Delete
class CalculateDistance:
    def distance(datafile):
        Delete.deleteContent()
        for data in datafile["customer"]:
        #print(p['longitude'])
            R = 6373.0

            lat1 = radians(53.339428)
            lon1 = radians(-6.257664)
            lat = float(data['latitude'])
            lat2 = radians(lat)
            lon = float(data['longitude'])
            lon2 = radians(lon)

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c

            if (distance<100):
                print(data['user_id'],data['name'])
                with open('C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\resultvs.txt', 'a') as f:
                   # f.seek(0)
                   # f.truncate()
                    f.write("%s\n" % data['name'])
                    f.close()
        return "file sucessfully created"
