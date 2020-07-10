import urllib.request,json
from dataPreparation import DataPreparation
class Fetchdata:
    def dataFromUrl():
        with urllib.request.urlopen("https://s3.amazonaws.com/intercom-take-home-test/customers.txt") as url:
            data = url.read()    
            file = open('C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\testvs.text', 'wb') 
            file.write(data) 
            file.close()
        

        with open('C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\testvs.text', 'r') as i:
            with open('C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\outputvs.txt', 'w') as j:
                for line in i:
                    line = line.rstrip('\n') + ','
                    print(line, file=j)
            print("data now has to be prepared to convert it in to Json file")
        DataPreparation.DataPreparationForJson()
