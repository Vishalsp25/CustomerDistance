
from JasonFile import JsonFile
class DataPreparation:
    def DataPreparationForJson():
        dataFile="C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\outputvs.txt"

        lines = open(dataFile, 'r').readlines()

        lines[0]="{"+"\"customer\""+":"+"["+lines[0]
        
        last_line = (lines[-1][:-2])+"]}"
        lines[-1] = last_line

        open(dataFile, 'w').writelines(lines)
       
        JsonFile.writeData()
    
